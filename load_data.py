from random import shuffle
from nltk import FreqDist

"""
My code should abstract the following places so others can use it freely:
APIS:
+a - tokenized data from files + (optional) mapping
+b - trained model from tokenized data + mapping + (optional) non-contextual
c - model activations from model weights (inc simple embeddings) + tokenized data + mapping
d - interpretation from model activations + tokenized data + mapping

If you want to use pre-trained (non-contextual) embeddings, for example:
1. Supply your own word_to_idx mapping to a that maps str tokens to indices based on your embeddings matrix
And overwrite the embedding matrix in b with your embeddings with my supplied function
or
2. Supply your own model weights and only use c, d

If you want to use contextual embeddings (BERT), for example, you can either:
1. Add word pieces to a, bert to b, c (requires understanding and changing my code)
or
2. Supply your own model activations and only use d
"""


# this is (a)
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

    with open(config["test_x_path"], "r", encoding="UTF-8") as f:
        data["test_x"] = [x.strip().split(u' ') for x in f]

    with open(config["train_y_path"], "r") as f:
        data["train_y"] = [int(x) - 1 for x in f]

    with open(config["test_y_path"], "r") as f:
        data["test_y"] = [int(x) - 1 for x in f]

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
    data["test_x"] = [[data["word_to_idx"].get(w, data["word_to_idx"]["@@UNK@@"]) for w in s] for s in data["test_x"]]

    return data

