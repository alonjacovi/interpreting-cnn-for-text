from random import shuffle
from nltk import FreqDist


def load_data(config, word_to_idx=None):
    """
    If you want to use embeddings, supply your own word_to_idx dict.
    If you want to use word piece splitting, the data files should already be split (space delimited)
    (in general, the data files should already be split and space delimited by whatever splitting you want)

    :param config: config dict
    :param word_to_idx: (optional) mapping from vocab to tokenized indices.
    :return:
    """
    data = {}

    with open(config["train_x_path"], "r", encoding="UTF-8") as f:
        data["train_x"] = [x.strip().split(u' ') for x in f]

    with open(config["train_y_path"], "r") as f:
        data["train_y"] = [int(x) - 1 for x in f]

    with open(config["valid_x_path"], "r", encoding="UTF-8") as f:
        data["valid_x"] = [x.strip().split(u' ') for x in f]

    with open(config["valid_y_path"], "r") as f:
        data["valid_y"] = [int(x) - 1 for x in f]

    if "pred_x_path" in config and "pred_y_path" in config:
        with open(config["pred_x_path"], "r", encoding="UTF-8") as f:
            data["pred_x"] = [x.strip().split(u' ') for x in f]

        with open(config["pred_y_path"], "r") as f:
            data["pred_y"] = [int(x) - 1 for x in f]

    if word_to_idx is None:
        all_words = [word for seq in data["train_x"] for word in seq]  # no test set here
        if "rare_word_threshold" in config:
            word_count = FreqDist(all_words)
            common_words = [x for x in word_count if word_count[x] > config["rare_word_threshold"]]
        else:
            common_words = all_words

        data["vocab"] = sorted(list(set(common_words)))
        data["word_to_idx"] = {w: (i + 2) for i, w in enumerate(data["vocab"])}
        data["idx_to_word"] = {k: v for v, k in data["word_to_idx"].items()}
        data["vocab"] = data["vocab"] + ["@@PAD@@"] + ["@@UNK@@"]
        data["word_to_idx"]["@@PAD@@"] = 0
        data["idx_to_word"][0] = "@@PAD@@"
        data["word_to_idx"]["@@UNK@@"] = 1
        data["idx_to_word"][1] = "@@UNK@@"
        data["classes"] = sorted(list(set(data["train_y"])))
    else:
        data["word_to_idx"] = word_to_idx
        data["vocab"] = sorted(list(word_to_idx))
        data["idx_to_word"] = {k: v for v, k in data["word_to_idx"].items()}
        data["classes"] = sorted(list(set(data["train_y"])))

    # tokenize data
    data["train_x"] = [[data["word_to_idx"].get(w, data["word_to_idx"]["@@UNK@@"]) for w in s] for s in data["train_x"]]
    data["valid_x"] = [[data["word_to_idx"].get(w, data["word_to_idx"]["@@UNK@@"]) for w in s] for s in data["valid_x"]]

    if "pred_x_path" in config and "pred_y_path" in config:
        data["pred_x"] = [[data["word_to_idx"].get(w, data["word_to_idx"]["@@UNK@@"]) for w in s] for s in data["pred_x"]]

    return data


def get_epoch(x, y, batch_size, is_train=True, padding_idx=0, num_examples=None):
    """
    Very simple random batching

    Returns batches of: sequences (padded to longest in batch), labels, and lengths
    """
    assert len(x) == len(y)

    if is_train:
        dataset = list(zip(x, y))
        shuffle(dataset)
        x, y = zip(*dataset)

    if num_examples is None:
        num_examples = len(x)

    batches_x = [x[i:i + batch_size] for i in range(0, num_examples, batch_size)]
    batches_y = [y[i:i + batch_size] for i in range(0, num_examples, batch_size)]

    lengths_x = []
    for i in range(len(batches_x)):
        batch = batches_x[i]
        lengths_x.append([len(s) for s in batch])
        max_s = max([len(s) for s in batch])
        batch = [s + [padding_idx] * (max_s - len(s)) for s in batch]
        batches_x[i] = batch

    return batches_x, batches_y, lengths_x

