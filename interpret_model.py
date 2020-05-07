import json
from data import load_data, get_epoch
import torch
import math
from torch import nn
import os
import numpy as np
import argparse

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter
from sklearn.cluster import MeanShift, estimate_bandwidth, DBSCAN


def eval_epoch_with_thresholds(model, data, config, thresholds):
    """
    Evaluate the thresholded model on the validation set
    """
    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["valid_x"], data["valid_y"], config["batch_size"], is_train=False)
    epoch_loss = 0
    corrects = 0
    criterion = nn.CrossEntropyLoss()

    thresh = [torch.FloatTensor(thresh_row) for thresh_row in thresholds["thresholds"]]
    if config["cuda"]:
        thresh = [t.cuda() for t in thresh]

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        pred = model(batch_x, thresh)['logits']
        loss = criterion(pred, batch_y)
        n_iter += 1
        epoch_loss += float(loss)

        batch_corrects = int((torch.max(pred, 1)[1].view(batch_y.size()).data == batch_y.data).sum())
        corrects += batch_corrects

        # if n_iter % 200 == 0:
        #     print(n_iter)
        del batch_x, batch_y, pred, loss

    return epoch_loss / len(data["valid_y"]), corrects / len(data["valid_y"]) * 100


def prettify_prediction_interpretation(interpretation_info, prediction_interpretation, config):
    """
    Convert the prediction interpretation to a pretty markdown string.
    The text coloring only supports up to 6 colors, i.e. up to 6 classes of labels. If you want more, it's easy
    to add.

    Format per instance:
    * original text
    * marked text: each token is preceded by a colored @ with a color corresponding to the class of the filter
      that "chose" an ngram containing this token.
    * a table of all the prediction data:
      filter name | filter identity class | passes | ngram | activation | slots

      - filter name format: w{ngram size}.f{filter index} ex. w3.f4 = filter number
        4 among the filters processing ngrams of size 3
      - passes: whether the ngram passes the threshold of this filter
      - activation: the final activation of the filter on this ngram. note that this number does NOT equal the sum of
        the slot activations, because it includes the filter bias weight and is after the ReLU layer (non-negative)
      - slots: the slot activation vector, i.e. the token-level activations gathered from breaking the filter-ngram
        dot-product into k dot-products (for ngram of length k)
    """
    output_str = "# Prediction info"

    def mark_span(sentence, span_start, span_end, color):
        mark = f'<span style="background-color: {color}">@</span>'
        marked_ngram = []
        for token in sentence[span_start:span_end]:
            if mark in token:
                marked_ngram.append(token)
            else:
                marked_ngram.append(mark + token)
        return sentence[:span_start] + marked_ngram + sentence[span_end:]

    colors = ["#FFFF00", "#6698FF", "#E56717", "#00FF7F", "#FFA07A", "#FF8C00"]  # add more colors here
    class_to_color = {}
    for cl, color in zip(list(config["class_to_str"]), colors):
        class_to_color[cl] = color

    identity_classes = interpretation_info["threshold_info"]["identity_classes"]
    thresholds = interpretation_info["threshold_info"]["thresholds"]

    for pinfo in prediction_interpretation:
        sen = pinfo["sentence"]

        table = "filter | filter class | passes | ngram | activation | slots\n"
        table += ":-- | :-- | :-- | :-- | :-- | :--\n"
        for wix, w_size in enumerate(config["ngram_sizes"]):
            for fix in range(config["num_filters"]):
                fname = "w" + str(w_size) + ".f" + str(fix)
                ngram = " ".join(pinfo[fname]["chosen_ngram"])
                ngram_span = pinfo[fname]["chosen_ngram_span"]

                c = identity_classes[fname]

                passes = "x" if pinfo[fname]["activation"] > thresholds[wix, fix] else " "

                if passes == "x":
                    sen = mark_span(sen, ngram_span[0], ngram_span[1], class_to_color[str(c)])

                l = " | ".join(
                    [fname, config["class_to_str"][str(c)], passes, "`" + ngram + "`",
                     "{0:.2f}".format(pinfo[fname]["activation"]),
                     str(["{0:.2f}".format(i) for i in pinfo[fname]["slot_activations"]])]) + "\n"
                table += l

        header = "## Original input: \n"
        header += "``` " + " ".join(pinfo["sentence"]) + " ``` \n\n"
        header += "## Marked input: \n"
        header += "<pre>" + " ".join(sen) + "</pre> \n\n"
        header += "Gold: " + pinfo["gold_str"] + ", Prediction: " + pinfo["prediction_str"] + "\n\n"

        output_str += "\n" + header + "\n" + table

    return output_str


def interpret_predictions(data, model, config):
    """
    Get a list of prediction interpretations. Each instance in the list contains:
    * The input sentence
    * The gold label
    * The predicted label
    * For each filter:
      - The chosen ngram (by max-pooling)
      - The ngram's activation at the max-pooling layer (AFTER adding the filter bias + AFTER a ReLU layer)
      - The slot activation vector for the ngram
    """
    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["pred_x"], data["pred_y"], 1, is_train=False)

    prediction_info = []

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        out = model(batch_x)

        pinfo = {}

        params = config

        # activations_filters = out['activations_filters']  # features
        # features = activations_filters
        ngram_indices = out['ngram_indices']
        activations_filters_pooled = out['activations_filters_pooled']  # pooled
        pooled = activations_filters_pooled
        logits = out['logits']

        indexed_seq = [int(x) for x in batch_x[0]]
        str_seq = [data["idx_to_word"][w] for w in indexed_seq]

        prediction = int(logits.squeeze().max(0)[1].item())
        prediction_str = config['class_to_str'][str(prediction)]
        gold = int(batch_y)
        gold_str = config['class_to_str'][str(gold)]

        pinfo["sentence"] = str_seq
        pinfo["gold"] = gold
        pinfo["gold_str"] = gold_str
        pinfo["prediction"] = prediction
        pinfo["prediction_str"] = prediction_str

        ngram_indices = [[int(x) for x in indices.squeeze()] for indices in ngram_indices]
        pooled_vals = [[float(x) for x in p.squeeze()] for p in pooled]
        filters = model.get_filters()

        max_ngram_len = max(params["ngram_sizes"])
        for ngram_len_idx, ngram_len in enumerate(params["ngram_sizes"]):
            seq = ['@@PAD@@'] * (max_ngram_len - 1) + str_seq + ['@@PAD@@'] * (max_ngram_len - 1)
            indexed_seq_padded = [data['word_to_idx']['@@PAD@@']] * (max_ngram_len - 1) + indexed_seq \
                                 + [data['word_to_idx']['@@PAD@@']] * (max_ngram_len - 1)

            for jx, ngram_ix in enumerate(ngram_indices[ngram_len_idx]):
                indexed_ngram = indexed_seq_padded[ngram_ix:ngram_ix + ngram_len]

                f, b = filters[ngram_len_idx]
                windows = [f[jx][k:k + params["embedding_dim"]] for k in range(0, f.size()[1], params["embedding_dim"])]
                # bias = b[jx]
                E = model.get_embeddings()
                ngram_embeddings = [E[k] for k in indexed_ngram]

                word_values = [float(torch.dot(a, b)) for a, b in zip(windows, ngram_embeddings)]

                fname = "w" + str(ngram_len) + ".f" + str(jx)

                if fname not in pinfo:
                    pinfo[fname] = {}
                pinfo[fname]["chosen_ngram_span"] = [ngram_ix, ngram_ix + ngram_len]
                pinfo[fname]["chosen_ngram"] = seq[ngram_ix:ngram_ix + ngram_len]
                pinfo[fname]["slot_activations"] = word_values
                pinfo[fname]["activation"] = pooled_vals[ngram_len_idx][jx]

        prediction_info.append(pinfo)

        n_iter += 1

        del batch_x, batch_y, lengths_x, out

    return prediction_info


def get_activations(data, model, config, sample_size=None):
    """
    This function goes over the data, one by one (batch size = 1), getting the max-pooled ngrams/activations,
    slot activations, and organizes them into a dict object for the "model interpretation" functions for the purpose
    of capturing the semantic meaning of each filter and calculating thresholds.
    """

    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["train_x"], data["train_y"], 1,
                                            is_train=False, num_examples=sample_size)

    interpretation_info = {
        "slot_activations": {},
        "chosen_ngrams_by_filter": {},
        "predicted_class": {}
    }

    for ngram_size in config["ngram_sizes"]:
        for filter_ix in range(config["num_filters"]):
            fname = "w" + str(ngram_size) + ".f" + str(filter_ix)
            interpretation_info["slot_activations"][fname] = []
            interpretation_info["chosen_ngrams_by_filter"][fname] = []
            interpretation_info["predicted_class"][fname] = []

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        out = model(batch_x)

        # activations_filters = out['activations_filters']
        ngram_indices = out['ngram_indices']
        # activations_filters_pooled = out['activations_filters_pooled']
        logits = out['logits']

        indexed_seq = [int(x) for x in batch_x[0]]
        str_seq = [data["idx_to_word"][w] for w in indexed_seq]

        prediction = int(logits.squeeze().max(0)[1].item())

        ngram_indices = [[int(x) for x in indices.squeeze()] for indices in ngram_indices]
        filters = model.get_filters()

        max_w_size = max(config["ngram_sizes"])
        for w_size_ix, w_size in enumerate(config["ngram_sizes"]):
            seq = ['@@PAD@@'] * (max_w_size - 1) + str_seq + ['@@PAD@@'] * (max_w_size - 1)
            indexed_seq_padded = [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1) + indexed_seq \
                                 + [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1)

            for jx, ngram_ix in enumerate(ngram_indices[w_size_ix]):
                indexed_ngram = indexed_seq_padded[ngram_ix:ngram_ix + w_size]

                f, b = filters[w_size_ix]
                windows = [f[jx][k:k + config["embedding_dim"]] for k in range(0, f.size()[1], config["embedding_dim"])]
                # bias = b[jx]
                E = model.get_embeddings()
                ngram_embeddings = [E[k] for k in indexed_ngram]

                assert len(windows) == len(ngram_embeddings)
                slot_acts = [float(torch.dot(a, b)) for a, b in zip(windows, ngram_embeddings)]
                slot_acts = {str(vx): v for vx, v in enumerate(slot_acts)}

                # Uncomment to verify that this code is correct
                # i.e., the sum of slot activations + filter bias = pooled activation from model
                # #### ####
                # assert math.isclose(max(sum(word_values) + float(b[jx].item()), 0), pooled_vals[w_size_ix][jx],
                #                     rel_tol=1e-05, abs_tol=1e-05):

                fname = "w" + str(w_size) + ".f" + str(jx)

                interpretation_info["slot_activations"][fname].append(slot_acts)
                interpretation_info["chosen_ngrams_by_filter"][fname].append(seq[ngram_ix:ngram_ix + w_size])
                interpretation_info["predicted_class"][fname].append(prediction)

        n_iter += 1

        del batch_x, batch_y, lengths_x, out

    for fname in interpretation_info["slot_activations"]:
        interpretation_info["slot_activations"][fname] \
            = np.array([list(vals_dict.values()) for vals_dict in interpretation_info["slot_activations"][fname]])
        interpretation_info["predicted_class"][fname] = np.array(interpretation_info["predicted_class"][fname])

    return interpretation_info


def calculate_threshold(sorted_predictions, purity_class, minimum_purity):
    """
    Get the threshold with the purity heuristic.

    Purity is defined as the precision metric where, where the threshold is treated as a binary classifier for the
    task of deciding whether an ngram is important or not - i.e., whether the label of the original sentence matches
    the identity class of the filter.

    :param sorted_predictions: all of the predictions of the interpretation dataset,
           sorted by the activation strength of the max-pooling layer of the filter in question
    :param purity_class: the identity class of the filter in question
    :param minimum_purity: the minimum purity value to be achieved by the threshold
    :return: the lowest threshold that satisfies the purity level
    """
    ix = len(sorted_predictions) - 1

    count = sum(sorted_predictions[:ix] == purity_class)
    purity = count / ix

    while purity < minimum_purity:
        ix -= 1
        if ix <= 0:
            return 0, 0

        if sorted_predictions[ix] == purity_class:
            count -= 1

        purity = count / ix

    return ix, purity


def model_interpretation_1(model, data, interpretation_info, config):
    filters = model.get_filters()
    W, b = model.get_fc_weights()
    embeddings = model.get_embeddings()

    for (filters_layer, layer_biases), (layer_index, layer_name) in zip(filters, enumerate(config["ngram_sizes"])):
        for jx, f in enumerate(filters_layer):
            fname = "w" + str(layer_name) + ".f" + str(jx)
            f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/filter_info.md", "w", encoding="UTF-8")

            window = [f[i:i + config["embedding_dim"]] for i in range(0, filters_layer.size()[1], config["embedding_dim"])]
            bias = layer_biases[jx]

            amount = config["top_k_in_logs"]
            top_names = [[] for _ in range(amount)]
            names_max = [[] for _ in range(amount)]
            bottom_names = [[] for _ in range(amount)]
            names_min = [[] for _ in range(amount)]

            for word_ix, word_filter in enumerate(window):
                dist = embeddings.matmul(word_filter).cpu().detach().numpy()

                arg_sort = np.argsort(dist)

                max_val, arg_max = [], []
                for a_val in arg_sort[::-1]:
                    m_val = dist[a_val]
                    if data["idx_to_word"][int(a_val)] in data["vocab"]:
                        max_val.append(m_val)
                        arg_max.append(a_val)
                        if len(max_val) == amount:
                            break

                min_val, arg_min = [], []
                for a_val in arg_sort:
                    m_val = dist[a_val]
                    if data["idx_to_word"][int(a_val)] in data["vocab"]:
                        min_val.append(m_val)
                        arg_min.append(a_val)
                        if len(min_val) == amount:
                            break

                for i in range(amount):
                    if len(arg_max) < i + 1:
                        top_names[i].append("N/A")
                        names_max[i].append(-1)
                    else:
                        top_names[i].append(data["idx_to_word"][int(arg_max[i])])
                        names_max[i].append(float(max_val[i]))

                for i in range(amount):
                    if len(arg_min) < i + 1:
                        bottom_names[i].append("N/A")
                        names_min[i].append(-1)
                    else:
                        bottom_names[i].append(data["idx_to_word"][int(arg_min[i])])
                        names_min[i].append(float(min_val[i]))

            print("# " + fname, file=f_out)

            print("#### Weights", file=f_out)
            print("Name | Value | Description", file=f_out)
            print(":--: | :--: | :--:", file=f_out)
            print(f"CNN bias | {bias.item()} | The bias value for this filter in the conv layer", file=f_out)
            jxx = config["num_filters"] * layer_index + jx
            for cl in config["class_to_str"]:
                print(f"{config['class_to_str'][cl]} (index: {int(cl)}) | {W[int(cl)][jxx].item()}"
                      f"| The weight of the class for this filter in the FC layer", file=f_out)
                print(f"{config['class_to_str'][cl]} bias | {b[int(cl)].item()}"
                      f"| The bias weight of the class for this filter in the FC layer", file=f_out)

            print("### Biggest words by slot", file=f_out)
            num_slots = int(layer_name)
            header = "Slot: |" + ' | '.join(["#" + str(slot) + " | val" for slot in range(num_slots)])
            print(header, file=f_out)
            print(":--: | " + ' | '.join([":--:" for _ in range(num_slots * 2)]), file=f_out)

            for i in range(amount):
                print(str(i) + ": |", " | ".join([w + " | " + str(val) for w, val in zip(top_names[i], names_max[i])]),
                      file=f_out)

            print("### Smallest words by slot", file=f_out)
            num_slots = int(layer_name)
            header = "Slot: |" + ' | '.join(["#" + str(slot) + " | val" for slot in range(num_slots)])
            print(header, file=f_out)
            print(":--: | " + ' | '.join([":--:" for _ in range(num_slots * 2)]), file=f_out)
            for i in range(amount):
                print(str(i) + ": |", " | ".join([w + " | " + str(val) for w, val in zip(bottom_names[i], names_min[i])]),
                      file=f_out)


def model_interpretation_2(model, interpretation_info, config):
    slot_activations = interpretation_info["slot_activations"]
    chosen_ngrams_by_filter = interpretation_info["chosen_ngrams_by_filter"]
    predicted_class = interpretation_info["predicted_class"]

    W, b = model.get_fc_weights()

    threshold_info = {}
    threshold_info["thresholds"] = np.array([[0.] * config["num_filters"]] * len(config["ngram_sizes"]))
    threshold_info["thresholds_x"] = {}
    threshold_info["average_coverage"] = 0.
    threshold_info["coverage_percentages_flat"] = np.array([0.] * (config["num_filters"] * len(config["ngram_sizes"])))
    threshold_info["purities"] = {}
    threshold_info["coverages"] = {}
    threshold_info["identity_classes"] = {}

    for fname in slot_activations:
        f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/filter_info_2.md", "w",
                     encoding="UTF-8")
        print('## Filter:', fname, file=f_out)
        print('filter:', fname)

        X = slot_activations[fname]

        ngrams = chosen_ngrams_by_filter[fname]
        ngrams_s = sorted(zip(X, ngrams), key=lambda ix: float(ix[0].sum()))[::-1]
        ngrams = [ngram for ix, ngram in ngrams_s]

        preds = predicted_class[fname]
        preds_s = sorted(zip(X, preds), key=lambda ix: float(ix[0].sum()))[::-1]
        predicted_class[fname] = [pred for ix, pred in preds_s]

        my_ngrams = np.array([' '.join(ngram).encode('ascii', 'ignore') for ngram in ngrams], dtype=np.string_)
        X = np.array([ix for ix, ngram in ngrams_s])

        fix_ = int(fname.split('.')[1][1:])
        w_size_idx = config["ngram_sizes"].index(int(fname.split('.')[0][1:]))
        fix = w_size_idx * config["num_filters"] + fix_
        fval = torch.max(W[:, fix], 0)[1]
        v = np.array(predicted_class[fname]).astype(int)

        print("#### Threshold", file=f_out)
        print("x (%) | y | r", file=f_out)
        print(":--: | :--: | :--:", file=f_out)

        r = config["minimum_purity"]
        t, p = calculate_threshold(v, fval.item(), r)

        if t <= 5:
            print("Bad filter: ", fname, fix)
            print(t, "(" + str(t // len(X)) + ")", "|", "Bad filter", "|", p, file=f_out)
        else:
            thresh_val = sum(X[t])
            print(t, "(" + str(int(t / len(X) * 100)) + "%)", "|", thresh_val, "|", p, file=f_out)
            print("threshold:", "x:", t, "y:", thresh_val, "purity:", p)

        threshold_info["thresholds"][w_size_idx, fix_] = sum(X[t])
        threshold_info["average_coverage"] += t / len(X) * 100
        threshold_info["coverage_percentages_flat"][fix] = t / len(X) * 100
        threshold_info["thresholds_x"][fix] = t
        threshold_info["purities"][fname] = p * 100
        threshold_info["coverages"][fname] = t / len(X) * 100
        threshold_info["identity_classes"][fname] = fval.item()

        if t == 0:
            t = 1
        X = X[:t]  # Threshold
        ngrams = ngrams[:t]  # Threshold
        my_ngrams = my_ngrams[:t]  # Threshold

        X_averages = X.mean(0)

        print("##### Biggest ngrams:", file=f_out)
        print("place | ngram | " + " | ".join(["Slot #" + str(k) + " val" for k in range(len(X[0]))]) + " | sum",
              file=f_out)
        print(":--: | :--: | " + " | ".join([":--:"] * len(X[0])) + " | :--: ", file=f_out)
        print("Avg | | " + " | ".join([str(k) for k in X_averages]) + " | | ", file=f_out)

        printed = []
        for ix, ngram in enumerate(ngrams):
            ngramstr = ' '.join(ngram).strip()
            if ngramstr not in printed:
                print(str(len(printed) + 1) + " | " + ngramstr + " | " + " | ".join(
                    [str(k) for k in X[ix]]) + " | " + str(sum(X[ix])), file=f_out)
                printed.append(ngramstr)
            if len(printed) == config["top_k_in_logs"]:
                break

        print("##### Most common words by slot (count in brackets)", file=f_out)
        print("Slot | " + " | ".join([str(k) for k in range(30)]), file=f_out)
        print(" :--: | " + " | ".join([":--:"] * 30), file=f_out)

        ngrams_transposed = [[] for _ in range(len(ngrams[0]))]
        for point_ix, point in enumerate(X):  # , cluster_ngrams):
            for wi, w in enumerate(ngrams[point_ix]):
                ngrams_transposed[wi].append(w)
        for wi, wi_list in enumerate(ngrams_transposed):
            freqs = Counter(wi_list)

            print("#" + str(wi) + " | " + " | ".join([y + " (" + str(c) + ")" for y, c in freqs.most_common(30)]),
                  file=f_out)

        print("##### Biggest words by slot (value in brackets)", file=f_out)
        print("Slot | " + " | ".join([str(k) for k in range(30)]), file=f_out)
        print(" :--: | " + " | ".join([":--:"] * 30), file=f_out)

        for wix in range(len(X_averages)):
            _, idx = np.unique(X[:, wix], return_index=True)
            b = np.array(X[:, wix])
            b[idx] = 0
            c = X[:, wix] - b
            biggest_words_ix = c.argsort()[-30:][::-1]
            biggest_words = [str(my_ngrams[biggest_word_ix], encoding='ascii').split(' ')[wix] for biggest_word_ix in
                             biggest_words_ix]
            biggest_values = [c[biggest_word_ix] for biggest_word_ix in biggest_words_ix]

            print("#" + str(wix) + " | " + " | ".join(
                [y + " (" + str(c) + ")" for y, c in zip(biggest_words, biggest_values) if c > 0.0]), file=f_out)

    f_out.close()

    threshold_info["average_coverage"] /= (config["num_filters"] * len(config["ngram_sizes"]))

    return threshold_info


def model_interpretation_3_clustering(model, interpretation_info, thresholds, config):
    slot_activations = interpretation_info["slot_activations"]
    chosen_ngrams_by_filter = interpretation_info["chosen_ngrams_by_filter"]
    predicted_class = interpretation_info["predicted_class"]

    num_clusters_flat = np.array([0.] * (config["num_filters"] * len(config["ngram_sizes"])))

    for fname in slot_activations:
        f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/cluster_info.md", "w",
                     encoding="UTF-8")
        print('## Filter:', fname, file=f_out)
        print('filter:', fname)

        X = slot_activations[fname]

        ngrams = chosen_ngrams_by_filter[fname]
        ngrams_s = sorted(zip(X, ngrams), key=lambda ix: float(ix[0].sum()))[::-1]
        ngrams = [ngram for ix, ngram in ngrams_s]

        preds = predicted_class[fname]
        preds_s = sorted(zip(X, preds), key=lambda ix: float(ix[0].sum()))[::-1]
        predicted_class[fname] = [pred for ix, pred in preds_s]

        my_ngrams = np.array([' '.join(ngram).encode('ascii', 'ignore') for ngram in ngrams], dtype=np.string_)
        X = np.array([ix for ix, ngram in ngrams_s])

        fix_ = int(fname.split('.')[1][1:])
        w_size_idx = config["ngram_sizes"].index(int(fname.split('.')[0][1:]))
        fix = w_size_idx * config["num_filters"] + fix_

        t = thresholds["thresholds_x"][fix]

        if t < 100:
            print("Skipping clustering due to too little ngrams that passed the threshold.")
            print("### Too little samples passed the threshold ({}). Skipping clustering".format(t), file=f_out)
            continue

        X = X[:t]  # Threshold
        ngrams = ngrams[:t]  # Threshold
        my_ngrams = my_ngrams[:t]  # Threshold

        ms = MeanShift()  # bin_seeding=True)
        ms.fit(X)

        labels = ms.labels_

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        num_clusters_flat[fix] = n_clusters_

        print("## Number of estimated clusters : %d" % n_clusters_, file=f_out)

        for k in range(n_clusters_):
            my_members = labels == k
            ngrams_transposed = [[] for _ in range(len(ngrams[0]))]
            X_members = X[my_members]

            X_averages = X_members.mean(0)
            print('### Cluster:', k, file=f_out)
            print('#### Cluster size in sample:', (len(X_members) / len(X) * 100), '%',
                  "[" + str(len(X_members)) + " / " + str(len(X)) + "]", file=f_out)

            print("##### Biggest ngrams:", file=f_out)
            print("place | ngram | " + " | ".join(["Slot #" + str(k) + " val" for k in range(len(X[0]))]) + " | sum",
                  file=f_out)
            print(":--: | :--: | " + " | ".join([":--:"] * len(X[0])) + " | :--: ", file=f_out)
            print("Avg | | " + " | ".join([str(k) for k in X_averages]) + " | | ", file=f_out)

            cnt = 0
            printed = []
            for point_ix, point in enumerate(X):  # , cluster_ngrams):
                if my_members[point_ix] == True:
                    ngramstr = ' '.join(ngrams[point_ix]).strip()
                    if (ngramstr not in printed) and cnt < config["top_k_in_logs"]:
                        print(str(len(printed) + 1) + " | " + ngramstr + " | " + " | ".join(
                            [str(k) for k in point]) + " | " + str(point.sum()), file=f_out)

                        cnt += 1
                        printed.append(ngramstr)
                    for wi, w in enumerate(ngrams[point_ix]):
                        ngrams_transposed[wi].append(w)

            print("##### Most common words by slot (count in brackets)", file=f_out)
            print("Slot | " + " | ".join([str(k) for k in range(30)]), file=f_out)
            print(":--: | " + " | ".join([":--:"] * 30), file=f_out)

            for wi, wi_list in enumerate(ngrams_transposed):
                freqs = Counter(wi_list)
                print("#" + str(wi) + " | " + " | ".join([y + " (" + str(c) + ")" for y, c in freqs.most_common(30)]),
                      file=f_out)

            print("##### Biggest words by slot (value in brackets)", file=f_out)
            print("Slot | " + " | ".join([str(k) for k in range(30)]), file=f_out)
            print(":--: | " + " | ".join([":--:"] * 30), file=f_out)

            for wix in range(len(X_averages)):
                _, idx = np.unique(X_members[:, wix], return_index=True)
                b = np.array(X_members[:, wix])
                b[idx] = 0
                c = X_members[:, wix] - b

                biggest_words_ix = c.argsort()[-6:][::-1]
                biggest_words = [str(my_ngrams[my_members][biggest_word_ix], encoding='ascii').split(' ')[wix] for
                                 biggest_word_ix in biggest_words_ix]
                biggest_values = [c[biggest_word_ix] for biggest_word_ix in biggest_words_ix]

                print("#" + str(wix) + " | " + " | ".join(
                    [y + " (" + str(c) + ")" for y, c in zip(biggest_words, biggest_values) if c > 0.0]), file=f_out)

        if int(fname.split('.')[0][1:]) == 2:
            # 2D plot
            plt.figure(1)  # , dpi=400)
            plt.clf()

            shapes = cycle('xo')
            colors = cycle('kgrcmykbgrcmykbgrcmykbgrcmyk')
            for k, col, shape in zip(range(n_clusters_), colors, shapes):
                my_members = labels == k
                plt.plot(X[my_members, 0], X[my_members, 1], 'x', col + shape, markersize=3)

            plt.savefig(config["model_path"] + "/model_interpretation/" + fname + '/clusters.pdf')

        elif int(fname.split('.')[0][1:]) == 3:
            # 3D plot
            fig = plt.figure(1)
            plt.clf()
            ax = fig.gca(projection='3d')

            shapes = cycle('xo')
            colors = cycle('kgrcmykbgrcmykbgrcmykbgrcmyk')
            for k, col, shape in zip(range(n_clusters_), colors, shapes):
                my_members = labels == k
                ax.scatter(X[my_members, 0], X[my_members, 1], X[my_members, 2], s=10, color=col,
                           marker=shape)  # + '.')

            plt.savefig(config["model_path"] + "/model_interpretation/" + fname + '/clusters.pdf')

    f_out.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-c", "--config", type=str, required=True)

    args = parser.parse_args()

    with open(args.config) as fp:
        interpretation_config = json.load(fp)

    model_path = interpretation_config["model_path"]
    with open(model_path+'/config.json') as fp:
        config = json.load(fp)

    config.update(interpretation_config)

    with open(model_path+'/w2i.json') as fp:
        w2i = json.load(fp)

    data = load_data(config=config, word_to_idx=w2i)

    if config["cuda"]:
        model = torch.load(model_path+'/model')
        model = model.cuda()
    else:
        model = torch.load(model_path+'/model', map_location=torch.device('cpu'))

    for ngram_size in config["ngram_sizes"]:
        for filter_ix in range(config["num_filters"]):
            fname = "w" + str(ngram_size) + ".f" + str(filter_ix)
            if not os.path.exists(interpretation_config["model_path"] + "/model_interpretation/" + fname):
                os.makedirs(interpretation_config["model_path"] + "/model_interpretation/" + fname)

    print("Getting training set activation data for interpretation...")
    interpretation_info = get_activations(data, model, config, sample_size=config["sample_size"])

    print("Token-level interpretation (biggest/smallest words per slot)...")
    model_interpretation_1(model, data, interpretation_info, config)

    print("Ngram-level interpretation and threshold calculation...")
    threshold_info = model_interpretation_2(model, interpretation_info, config)
    interpretation_info["threshold_info"] = threshold_info

    print("Evaluating thresholds...")
    loss, acc = eval_epoch_with_thresholds(model, data, config, threshold_info)
    print(f"Model with thresholds performance:\tLoss: {loss}\tAccuracy: {acc}")

    if "cluster" in config and config["cluster"]:
        print("Slot activation vector clustering...")
        model_interpretation_3_clustering(model, interpretation_info, threshold_info, config)

    print("Prediction interpretation...")
    prediction_interpretation = interpret_predictions(data, model, config)

    with open(config["model_path"] + "/prediction_interpretation.json", "w") as fp:
        json.dump(prediction_interpretation, fp=fp)

    print("Saving prediction interpretation to markdown...")
    with open(config["model_path"] + "/prediction_interpretation.md", "w") as fp:
        fp.write(prettify_prediction_interpretation(interpretation_info, prediction_interpretation, config))
