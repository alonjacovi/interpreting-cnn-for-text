# change model forward to output dict with activations

# argparse model folder
# load model
# get activations (evaluation on model with train? dev?) - analyze()
# model interpretation - filter clusters + thresholds - clusters()
# argparse data path
# data interpretation - bottom of script i think

import json
from data import load_data, get_epoch
import model
import torch
import math
from torch import nn
import torch.nn.functional as F
import os
import numpy as np
from random import shuffle
import logging

import matplotlib
matplotlib.use('agg')
# matplotlib.rcParams.update({'font.size': 18})
import matplotlib.pyplot as plt
from itertools import cycle
from mpl_toolkits.mplot3d import Axes3D
from collections import Counter
from sklearn.cluster import MeanShift, estimate_bandwidth, DBSCAN
# import pickle
# import hdbscan

logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(logging.INFO)


def eval_epoch_with_thresholds(model, data, config, thresholds):
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

        # optimizer.zero_grad()
        pred = model(batch_x, thresh)['logits']
        loss = criterion(pred, batch_y)
        n_iter += 1
        epoch_loss += float(loss)

        batch_corrects = int((torch.max(pred, 1)[1].view(batch_y.size()).data == batch_y.data).sum())
        corrects += batch_corrects

        # if n_iter % 200 == 0:
        #     eval()
        #     model.train()
        del batch_x, batch_y, pred, loss

    return epoch_loss / len(data["valid_y"]), corrects / len(data["valid_y"]) * 100


def prettify_prediction_interpretation(interpretation_info, prediction_interpretation, config):
    output_str = "# Prediction info"

    def mark_span(sentence, span_start, span_end, color):
        mark = f'<span style="background-color: {color}">@</span>'
        marked_ngram = [mark + token for token in sentence[span_start:span_end]]
        return sentence[:span_start] + marked_ngram + sentence[span_end:]

    colors = ["#FFFF00", "#6698FF", "#E56717", "#00FF7F", "#FFA07A", "#FF8C00"]
    class_to_color = {}
    for cl, color in zip(list(config["class_to_str"]), colors):
        class_to_color[cl] = color

    identity_classes = interpretation_info["threshold_info"]["identity_classes"]
    thresholds = interpretation_info["threshold_info"]["thresholds"]

    for pinfo in prediction_interpretation:
        sen = pinfo["sentence"]

        table = "filter | passes | ngram | activation | slots\n"
        table += ":-- | :-- | :-- | :-- | :--\n"
        for wix, w_size in enumerate(config["ngram_sizes"]):
            for fix in range(config["num_filters"]):
                fname = "w" + str(w_size) + ".f" + str(fix)
                ngram = " ".join(pinfo[fname]["chosen_ngram"])
                ngram_span = pinfo[fname]["chosen_ngram_span"]

                c = identity_classes[fname]

                # fix_ = wix * params["feature_num"] + fix
                passes = "x" if pinfo[fname]["activation"] > thresholds[wix, fix] else " "

                if passes == "x":
                    sen = mark_span(sen, ngram_span[0], ngram_span[1], class_to_color[str(c)])

                l = " | ".join(
                    [fname, passes, "`" + ngram + "`", "{0:.2f}".format(pinfo[fname]["activation"]),
                     str(["{0:.2f}".format(i) for i in pinfo[fname]["slot_activations"]])]) + "\n"
                table += l

        header = "### Original input: \n"
        header += "``` " + " ".join(pinfo["sentence"]) + " ``` \n\n"
        header += "### Marked input: \n"
        header += "<pre>" + " ".join(sen) + "</pre> \n\n"
        header += "Gold: " + pinfo["gold_str"] + ", Prediction: " + pinfo["prediction_str"] + "\n\n"

        output_str += "\n" + header + "\n" + table

    return output_str


def interpret_predictions(data, model, config):
    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["pred_x"], data["pred_y"], 1,
                                            is_train=False)

    prediction_info = []

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        # optimizer.zero_grad()
        out = model(batch_x)

        pinfo = {}

        params = config

        # activations_filters = out['activations_filters']  # features
        # features = activations_filters
        ngram_indices = out['ngram_indices']
        activations_filters_pooled = out['activations_filters_pooled']  # pooled
        pooled = activations_filters_pooled
        logits = out['logits']
        # pred = logits

        indexed_seq = [int(x) for x in batch_x[0]]
        str_seq = [data["idx_to_word"][w] for w in indexed_seq]
        real_seq = str_seq

        prediction = int(logits.squeeze().max(0)[1].item())
        prediction_str = config['class_to_str'][str(prediction)]
        gold = int(batch_y)
        gold_str = config['class_to_str'][str(gold)]

        # if save_predictions:
        pinfo["sentence"] = real_seq
        pinfo["gold"] = gold
        pinfo["gold_str"] = gold_str
        pinfo["prediction"] = prediction
        pinfo["prediction_str"] = prediction_str

        ngram_indices = [[int(x) for x in indices.squeeze()] for indices in ngram_indices]
        pooled_vals = [[float(x) for x in p.squeeze()] for p in pooled]
        filters = model.get_filters()

        max_w_size = max(params["ngram_sizes"])
        for w_size_ix, w_size in enumerate(params["ngram_sizes"]):
            seq = ['@@PAD@@'] * (max_w_size - 1) + real_seq + ['@@PAD@@'] * (max_w_size - 1)

            indexed_seq_padded = [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1) + indexed_seq \
                                 + [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1)

            for jx, ngram_ix in enumerate(ngram_indices[w_size_ix]):

                # ngram_str = (' '.join(seq[ngram_ix:ngram_ix + w_size])).strip()
                indexed_ngram = indexed_seq_padded[ngram_ix:ngram_ix + w_size]

                f, b = filters[w_size_ix]
                windows = [f[jx][k:k + params["embedding_dim"]] for k in range(0, f.size()[1], params["embedding_dim"])]
                # bias = b[jx]
                E = model.get_embeddings()
                ngram_embeddings = [E[k] for k in indexed_ngram]

                word_values = [float(torch.dot(a, b)) for a, b in zip(windows, ngram_embeddings)]

                fname = "w" + str(w_size) + ".f" + str(jx)

                if fname not in pinfo:
                    pinfo[fname] = {}
                # pinfo[fname]["chosen_ngram_str"] = ngram_str
                pinfo[fname]["chosen_ngram_span"] = [ngram_ix, ngram_ix + w_size]
                pinfo[fname]["chosen_ngram"] = seq[ngram_ix:ngram_ix + w_size]
                pinfo[fname]["slot_activations"] = word_values
                pinfo[fname]["activation"] = pooled_vals[w_size_ix][jx]  # TODO cast to python/numpy from torch?

        prediction_info.append(pinfo)

        n_iter += 1

        del batch_x, batch_y, lengths_x, out

    return prediction_info


def get_activations(data, model, config, sample_size=None):
    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["train_x"], data["train_y"], 1,
                                            is_train=False, num_examples=sample_size)

    interpretation_info = {
        "filter_word_sum": {},
        "filter_word_count": {},
        "sorted_word_values": {},
        "sorted_word_sums": {},
        "sorted_word_ngrams": {},
        "sorted_word_pred_class": {}
        # "prediction_info": []
    }

    for ngram_size in config["ngram_sizes"]:
        for filter_ix in range(config["num_filters"]):
            fname = "w" + str(ngram_size) + ".f" + str(filter_ix)
            interpretation_info["sorted_word_values"][fname] = []
            interpretation_info["sorted_word_sums"][fname] = []
            interpretation_info["sorted_word_ngrams"][fname] = []
            interpretation_info["sorted_word_pred_class"][fname] = []

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        # optimizer.zero_grad()
        out = model(batch_x)

        # pinfo = {}

        params = config

        activations_filters = out['activations_filters']  # features
        # features = activations_filters
        ngram_indices = out['ngram_indices']
        activations_filters_pooled = out['activations_filters_pooled']  # pooled
        pooled = activations_filters_pooled
        logits = out['logits']
        # pred = logits

        indexed_seq = [int(x) for x in batch_x[0]]
        str_seq = [data["idx_to_word"][w] for w in indexed_seq]
        real_seq = str_seq

        prediction = int(logits.squeeze().max(0)[1].item())
        # prediction_str = config['class_to_str'][str(prediction)]
        # gold = int(batch_y)
        # gold_str = config['class_to_str'][str(gold)]

        # if save_predictions:
        # pinfo["sentence"] = real_seq
        # pinfo["gold"] = gold
        # pinfo["gold_str"] = gold_str
        # pinfo["prediction"] = prediction
        # pinfo["prediction_str"] = prediction_str

        ngram_indices = [[int(x) for x in indices.squeeze()] for indices in ngram_indices]
        pooled_vals = [[float(x) for x in p.squeeze()] for p in pooled]
        filters = model.get_filters()

        max_w_size = max(params["ngram_sizes"])
        for w_size_ix, w_size in enumerate(params["ngram_sizes"]):
            if w_size not in interpretation_info["filter_word_sum"]:
                interpretation_info["filter_word_sum"][w_size] = {}
                interpretation_info["filter_word_count"][w_size] = {}
                # filter_word_pred_class[w_size] = {}

            seq = ['@@PAD@@'] * (max_w_size - 1) + real_seq + ['@@PAD@@'] * (max_w_size - 1)

            indexed_seq_padded = [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1) + indexed_seq \
                                 + [data['word_to_idx']['@@PAD@@']] * (max_w_size - 1)

            for jx, ngram_ix in enumerate(ngram_indices[w_size_ix]):
                if jx not in interpretation_info["filter_word_sum"][w_size]:
                    interpretation_info["filter_word_sum"][w_size][jx] = {k: 0.0 for k in range(w_size)}
                    interpretation_info["filter_word_count"][w_size][jx] = {k: 0 for k in range(w_size)}

                # ngram_str = (' '.join(seq[ngram_ix:ngram_ix + w_size])).strip()
                indexed_ngram = indexed_seq_padded[ngram_ix:ngram_ix + w_size]

                f, b = filters[w_size_ix]
                windows = [f[jx][k:k + params["embedding_dim"]] for k in range(0, f.size()[1], params["embedding_dim"])]
                # bias = b[jx]
                E = model.get_embeddings()
                ngram_embeddings = [E[k] for k in indexed_ngram]

                assert len(windows) == len(ngram_embeddings)
                word_values = [float(torch.dot(a, b)) for a, b in zip(windows, ngram_embeddings)]

                # Uncomment to verify that this code is correct
                # i.e., the sum of slot activations + filter bias = pooled activation from model
                # #### ####
                # assert math.isclose(max(sum(word_values) + float(b[jx].item()), 0), pooled_vals[w_size_ix][jx],
                #                     rel_tol=1e-05, abs_tol=1e-05):

                for word_value_ix, word_value in enumerate(word_values):
                    interpretation_info["filter_word_sum"][w_size][jx][word_value_ix] += word_value
                    interpretation_info["filter_word_count"][w_size][jx][word_value_ix] += 1

                word_values_tbdict = {str(vx): v for vx, v in enumerate(word_values)}

                fname = "w" + str(w_size) + ".f" + str(jx)

                interpretation_info["sorted_word_values"][fname].append(word_values_tbdict)
                interpretation_info["sorted_word_ngrams"][fname].append(seq[ngram_ix:ngram_ix + w_size])
                interpretation_info["sorted_word_pred_class"][fname].append(prediction)
                # sorted_word_sums[fname].append(pooled_vals[w_size_ix][jx])

                # if fname not in pinfo:
                #     pinfo[fname] = {}
                # pinfo[fname]["chosen_ngram"] = seq[ngram_ix:ngram_ix + w_size]
                # pinfo[fname]["slot_activations"] = word_values
                # pinfo[fname]["activation"] = pooled_vals[w_size_ix][jx]  # TODO cast to python/numpy from torch?

        # interpretation_info["prediction_info"].append(pinfo)

        n_iter += 1

        del batch_x, batch_y, lengths_x, out

    for fname in interpretation_info["sorted_word_values"]:
        interpretation_info["sorted_word_values"][fname] \
            = np.array([list(vals_dict.values()) for vals_dict in interpretation_info["sorted_word_values"][fname]])
        interpretation_info["sorted_word_pred_class"][fname] \
            = np.array(interpretation_info["sorted_word_pred_class"][fname])

    # print(interpretation_info)
    return interpretation_info


def calculate_threshold(v, purity_class, minimum_purity):
    """
    Get the threshold with the purity heuristic.

    Purity is defined as the precision metric where, where the threshold is treated as a binary classifier for the
    task of deciding whether an ngram is important or not - i.e., whether the label of the original sentence matches
    the identity class of the filter.

    :param v: all of the labels of the interpretation dataset, sorted by the activation strength of the
              max-pooling layer of the filter in question
    :param purity_class: the identity class of the filter in question
    :param minimum_purity: the minimum purity value to be achieved by the threshold
    :return: the lowest threshold that satisfies the purity level
    """
    ix = len(v) - 1

    count = sum(v[:ix] == purity_class)
    purity = count / ix
    while purity < minimum_purity:
        ix -= 1

        if ix <= 0:
            return 0, 0

        if v[ix] == purity_class:
            count -= 1

        purity = count / ix

    return ix, purity


def model_interpretation_1(model, data, interpretation_info, config):
    filters = model.get_filters()
    biases_flat = np.concatenate([layer_biases.cpu().data.numpy() for filters_layer, layer_biases in filters])
    W, b = model.get_fc_weights()
    embeddings = model.get_embeddings()
    a = {}
    max_filter_val = -float('inf')
    max_filter = None

    for (filters_layer, layer_biases), (layer_index, layer_name) in zip(filters, enumerate(config["ngram_sizes"])):
        # a[layer_name] = []

        for jx, f in enumerate(filters_layer):

            fname = "w" + str(layer_name) + ".f" + str(jx)
            f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/filter_info.md", "w", encoding="UTF-8")

            # print(f)
            window = [f[i:i + config["embedding_dim"]] for i in range(0, filters_layer.size()[1], config["embedding_dim"])]
            bias = layer_biases[jx]

            # if params["save_filter_info"]:
            #     filter_info[fname]["bias"] = bias.item()
            #     filter_info[fname]["convolution"] = f.detach().cpu().numpy()

            amount = config["top_k_in_logs"]
            names = [[] for _ in range(amount)]
            names_max = [[] for _ in range(amount)]
            bottom_names = [[] for _ in range(amount)]
            names_min = [[] for _ in range(amount)]

            # wordlist = ["not", "n't", "is", "are", "were"]
            # choice_names = [[] for _ in range(len(wordlist))]
            # choice_val = [[] for _ in range(len(wordlist))]

            name1, name2, name3 = [], [], []
            name1max, name2max, name3max = [], [], []
            # name1neg, name2neg, name3neg = [], [], []
            filter_word_averages = []

            # filter_val = 0

            for word_ix, word_filter in enumerate(window):
                dist = embeddings.matmul(word_filter).cpu().detach().numpy()

                # argmax = torch.max(dist, 0)[1]
                # print(dist)
                # max_val, argmax = dist.topk(len(dist), 0)
                argsort = np.argsort(dist)

                mm, aa = [], []
                # for m_val, a_val in zip(max_val, argmax):
                for a_val in argsort[::-1]:
                    m_val = dist[a_val]
                    # print(mm, aa, ":", m_val, a_val)
                    if data["idx_to_word"][int(a_val)] in data["vocab"]:
                        mm.append(m_val)
                        aa.append(a_val)
                        if len(mm) == amount:
                            # print("my my ")
                            break
                max_val, argmax = mm, aa

                mm, aa = [], []
                # for m_val, a_val in zip(min_val, argmin):
                for a_val in argsort:
                    m_val = dist[a_val]
                    # print(mm, aa, ":", m_val, a_val)
                    if data["idx_to_word"][int(a_val)] in data["vocab"]:
                        mm.append(m_val)
                        aa.append(a_val)
                        if len(mm) == amount:
                            # print("my my ")
                            break
                min_val, argmin = mm, aa

                # argmax = [x for x in argmax if int(x) in common_words]
                # max_val = [0,0,0]

                for i in range(amount):
                    if len(argmax) < i + 1:
                        names[i].append("N/A")
                        names_max[i].append(-1)
                    else:
                        names[i].append(data["idx_to_word"][int(argmax[i])])
                        names_max[i].append(float(max_val[i]))

                for i in range(amount):
                    if len(argmin) < i + 1:
                        bottom_names[i].append("N/A")
                        names_min[i].append(-1)
                    else:
                        bottom_names[i].append(data["idx_to_word"][int(argmin[i])])
                        names_min[i].append(float(min_val[i]))

                # for i in range(len(wordlist)):
                #     if wordlist[i] in data["word_to_idx"]:
                #         choice_names[i].append(wordlist[i])
                #         choice_val[i].append(dist[data["word_to_idx"][wordlist[i]]])

                filter_word_averages.append(
                    str(interpretation_info["filter_word_sum"][layer_name][jx][word_ix]
                        / interpretation_info["filter_word_count"][layer_name][jx][word_ix]))
                # filter_val += float(max_val[0])

            if sum(name1max) > max_filter_val:
                max_filter_val = sum(name1max)
                max_filter = name1

            print("# " + fname, file=f_out)
            # print("#### Linear layer bias:", b, file=f_out)

            # print("Bias | Pos | Neg", file=f_out)
            # print(":--: | :--: | :--:", file=f_out)
            # jxx = config["num_filters"] * layer_index + jx
            # print(bias.item(), "|", W[1][jxx].item(), "|", W[0][jxx].item(), file=f_out)

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
            print("Avg: |  |", ' |  | '.join(filter_word_averages), file=f_out)

            for i in range(amount):
                print(str(i) + ": |", " | ".join([w + " | " + str(val) for w, val in zip(names[i], names_max[i])]),
                      file=f_out)

            print("### Smallest words by slot", file=f_out)
            num_slots = int(layer_name)
            header = "Slot: |" + ' | '.join(["#" + str(slot) + " | val" for slot in range(num_slots)])
            print(header, file=f_out)
            print(":--: | " + ' | '.join([":--:" for _ in range(num_slots * 2)]), file=f_out)
            print("Avg: |  |", ' |  | '.join(filter_word_averages), file=f_out)
            for i in range(amount):
                print(str(i) + ": |", " | ".join([w + " | " + str(val) for w, val in zip(bottom_names[i], names_min[i])]),
                      file=f_out)


def model_interpretation_2(model, interpretation_info, config):
    sorted_word_values = interpretation_info["sorted_word_values"]
    sorted_word_ngrams = interpretation_info["sorted_word_ngrams"]
    sorted_word_pred_class = interpretation_info["sorted_word_pred_class"]

    W, b = model.get_fc_weights()

    # print('==== Sample name:', sample_name)

    thresholds = {}
    thresholds["thresholds"] = np.array([[0.] * config["num_filters"]] * len(config["ngram_sizes"]))
    # thresholds = np.array([[0.] * config["num_filters"]] * len(config["ngram_sizes"]))
    thresholds["thresholds_x"] = {}
    thresholds["average_coverage"] = 0.
    thresholds["coverage_percentages_flat"] = np.array([0.] * (config["num_filters"] * len(config["ngram_sizes"])))
    thresholds["purities"] = {}
    thresholds["coverages"] = {}
    thresholds["identity_classes"] = {}

    num_clusters_flat = np.array([0.] * (config["num_filters"] * len(config["ngram_sizes"])))

    for fname in sorted_word_values:
        f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/filter_info_2.md", "w",
                     encoding="UTF-8")
        print('## Filter:', fname, file=f_out)
        print('filter:', fname)

        X = sorted_word_values[fname]

        ngrams = sorted_word_ngrams[fname]
        ngrams_s = sorted(zip(X, ngrams), key=lambda ix: float(ix[0].sum()))[::-1]
        ngrams = [ngram for ix, ngram in ngrams_s]

        # for cl in sorted_word_pred_class[fname]:
        preds = sorted_word_pred_class[fname]
        preds_s = sorted(zip(X, preds), key=lambda ix: float(ix[0].sum()))[::-1]
        sorted_word_pred_class[fname] = [pred for ix, pred in preds_s]

        my_ngrams = np.array([' '.join(ngram).encode('ascii', 'ignore') for ngram in ngrams], dtype=np.string_)
        X = np.array([ix for ix, ngram in ngrams_s])

        fix_ = int(fname.split('.')[1][1:])
        w_size_idx = config["ngram_sizes"].index(int(fname.split('.')[0][1:]))
        fix = w_size_idx * config["num_filters"] + fix_
        fval = torch.max(W[:, fix], 0)[1]
        v = np.array(sorted_word_pred_class[fname]).astype(int)

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

        thresholds["thresholds"][w_size_idx, fix_] = sum(X[t])
        thresholds["average_coverage"] += t / len(X) * 100
        thresholds["coverage_percentages_flat"][fix] = t / len(X) * 100
        thresholds["thresholds_x"][fix] = t
        thresholds["purities"][fname] = p * 100
        thresholds["coverages"][fname] = t / len(X) * 100
        thresholds["identity_classes"][fname] = fval.item()

        if t == 0:
            t = 1
        # if len([config["minimum_purity"]]) > 1:
        X = X[:t]  # Threshold
        ngrams = ngrams[:t]  # Threshold
        my_ngrams = my_ngrams[:t]  # Threshold

        # X_sums = X.sum(1)
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

    thresholds["average_coverage"] /= (config["num_filters"] * len(config["ngram_sizes"]))

    return thresholds


def model_interpretation_3_clustering(model, interpretation_info, thresholds, config):
    sorted_word_values = interpretation_info["sorted_word_values"]
    sorted_word_ngrams = interpretation_info["sorted_word_ngrams"]
    sorted_word_pred_class = interpretation_info["sorted_word_pred_class"]

    W, b = model.get_fc_weights()

    # print('==== Sample name:', sample_name)
    # for fname in sorted_word_values:
    #     sorted_word_values[fname] = np.array([list(vals_dict.values()) for vals_dict in sorted_word_values[fname]])
    #     pred_class_mask_pos = np.array(list(map(lambda v: v == 'pos', sorted_word_pred_class[fname])))
    #     pred_class_mask_neg = np.array(list(map(lambda v: v == 'neg', sorted_word_pred_class[fname])))
    #     sorted_word_pred_class[fname] = {'pos': pred_class_mask_pos, 'neg': pred_class_mask_neg}

    num_clusters_flat = np.array([0.] * (config["num_filters"] * len(config["ngram_sizes"])))

    for fname in sorted_word_values:
        f_out = open(config["model_path"] + "/model_interpretation/" + fname + "/cluster_info.md", "w",
                     encoding="UTF-8")
        print('## Filter:', fname, file=f_out)
        print('filter:', fname)

        X = sorted_word_values[fname]

        ngrams = sorted_word_ngrams[fname]
        ngrams_s = sorted(zip(X, ngrams), key=lambda ix: float(ix[0].sum()))[::-1]
        ngrams = [ngram for ix, ngram in ngrams_s]

        # for cl in sorted_word_pred_class[fname]:
        preds = sorted_word_pred_class[fname]
        preds_s = sorted(zip(X, preds), key=lambda ix: float(ix[0].sum()))[::-1]
        sorted_word_pred_class[fname] = [pred for ix, pred in preds_s]

        my_ngrams = np.array([' '.join(ngram).encode('ascii', 'ignore') for ngram in ngrams], dtype=np.string_)
        X = np.array([ix for ix, ngram in ngrams_s])

        fix_ = int(fname.split('.')[1][1:])
        w_size_idx = config["ngram_sizes"].index(int(fname.split('.')[0][1:]))
        fix = w_size_idx * config["num_filters"] + fix_

        t = thresholds["thresholds_x"][fix]

        if t < 20:
            print("Skipping clustering")
            print("### Too little samples passed the threshold ({}). Skipping clustering".format(t), file=f_out)
            continue

        X = X[:t]  # Threshold
        ngrams = ngrams[:t]  # Threshold
        my_ngrams = my_ngrams[:t]  # Threshold

        # X_sums = X.sum(1)
        # X_averages = X.mean(0)

        X = X[:t]  # Threshold
        ngrams = ngrams[:t]  # Threshold
        my_ngrams = my_ngrams[:t]  # Threshold

        # X_sums = X.sum(1)
        # X_averages = X.mean(0)

        ms = MeanShift()  # bin_seeding=True)
        ms.fit(X)

        labels = ms.labels_
        # cluster_centers = ms.cluster_centers_ ####################### MEAN SHIFT

        labels_unique = np.unique(labels)
        n_clusters_ = len(labels_unique)

        num_clusters_flat[fix] = n_clusters_

        print("## Number of estimated clusters : %d" % n_clusters_, file=f_out)
        # print(ngrams)
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
    """
    TODO
    
    (v) Change top 30/50 to top 100 (or top k from config)
    Print prediction interpretation or output to markdown
    Meaningful names
    Better prints
    Documentation
    Final cleanup
    Test:
    1. cuda on train
    2. cuda on interpretation
    3. elec/amazon with larger model
    4. Something with more than 2 classes (can just change some numbers....)
    """

    with open("/home/nlp/jacovia/nlp_clust/rewrite/interpretation_config.json") as fp:
        interpretation_config = json.load(fp)

    model_path = interpretation_config["model_path"]
    with open(model_path+'/config.json') as fp:
        config = json.load(fp)

    config.update(interpretation_config)

    with open(model_path+'/w2i.json') as fp:
        w2i = json.load(fp)

    data = load_data(config=config, word_to_idx=w2i)

    model = torch.load(model_path+'/model')

    if config["cuda"]:
        model = model.cuda()

    for ngram_size in config["ngram_sizes"]:
        for filter_ix in range(config["num_filters"]):
            fname = "w" + str(ngram_size) + ".f" + str(filter_ix)
            if not os.path.exists(interpretation_config["model_path"] + "/model_interpretation/" + fname):
                os.makedirs(interpretation_config["model_path"] + "/model_interpretation/" + fname)

    print("Doing 0")

    interpretation_info = get_activations(data, model, config, sample_size=150)

    print("Doing 1")

    model_interpretation_1(model, data, interpretation_info, config)

    print("Doing 2")

    threshold_info = model_interpretation_2(model, interpretation_info, config)
    interpretation_info["threshold_info"] = threshold_info

    if "cluster" in config and config["cluster"]:
        model_interpretation_3_clustering(model, interpretation_info, threshold_info, config)

    print("Doing eval")

    loss, acc = eval_epoch_with_thresholds(model, data, config, threshold_info)
    print(f"Model with thresholds performance:\tLoss: {loss}\tAccuracy: {acc}")

    print("Doing pred")

    prediction_interpretation = interpret_predictions(data, model, config)

    with open(config["model_path"] + "/prediction_interpretation.json", "w") as fp:
        json.dump(prediction_interpretation, fp=fp)

    with open(config["model_path"] + "/prediction_interpretation.md", "w") as fp:
        fp.write(prettify_prediction_interpretation(interpretation_info, prediction_interpretation, config))

