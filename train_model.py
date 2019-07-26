import json
from data import load_data, get_epoch
import model
import torch
from torch import nn
import torch.nn.functional as F
import os
from random import shuffle
import logging
logger = logging.getLogger(__name__)  # pylint: disable=invalid-name
logger.setLevel(logging.INFO)


def train_epoch(model, data, config):
    model.train()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["train_x"], data["train_y"], config["batch_size"], is_train=True)
    epoch_loss = 0
    corrects = 0
    criterion = nn.CrossEntropyLoss()
    # corrects_neg, corrects_pos = 0, 0

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        optimizer.zero_grad()
        pred = model(batch_x)['logits']
        loss = criterion(pred, batch_y)
        n_iter += 1
        epoch_loss += float(loss)
        loss.backward()
        optimizer.step()

        batch_corrects = int((torch.max(pred, 1)[1].view(batch_y.size()).data == batch_y.data).sum())
        corrects += batch_corrects

        # if n_iter % 200 == 0:
        #     eval()
        #     model.train()

    return epoch_loss / len(data["train_y"]), corrects / len(data["train_y"]) * 100


def eval_epoch(model, data, config):
    model.eval()
    n_iter = 0
    epoch_x, epoch_y, lengths_x = get_epoch(data["valid_x"], data["valid_y"], config["batch_size"], is_train=False)
    epoch_loss = 0
    corrects = 0
    criterion = nn.CrossEntropyLoss()

    for batch_x, batch_y, length_x in zip(epoch_x, epoch_y, lengths_x):
        batch_x = torch.LongTensor(batch_x)
        batch_y = torch.LongTensor(batch_y)
        lengths_x = torch.LongTensor(length_x)

        if config["cuda"]:
            batch_x, batch_y, lengths_x = batch_x.cuda(), batch_y.cuda(), lengths_x.cuda()

        # optimizer.zero_grad()
        pred = model(batch_x)['logits']
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


if __name__ == '__main__':
    with open('/home/nlp/jacovia/nlp_clust/rewrite/config.json') as fp:
        config = json.load(fp)

    data = load_data(config=config)

    print(config)
    # print(len(data["vocab"]))
    # logger.info("Info...")

    model = model.CnnClassifier(ngram_sizes=config["ngram_sizes"], embedding_dim=config["embedding_dim"],
                                num_filters=config["num_filters"], padding_idx=data["word_to_idx"]["@@PAD@@"],
                                num_classes=len(data["classes"]), vocab_size=len(data["vocab"]))

    if "cuda" not in config:
        config["cuda"] = False

    if config["cuda"]:
        model = model.cuda()

    parameters = filter(lambda p: p.requires_grad, model.parameters())
    if "learning_rate" in config:
        optimizer = torch.optim.Adam(parameters, config["learning_rate"])
    else:
        optimizer = torch.optim.Adam(parameters)

    if not os.path.exists(config["model_path"]):
        os.makedirs(config["model_path"])

    print("\t".join(["Epoch", "Loss", "Acc", "Eval", "Acc", "Best"]))
    metrics = {"loss": [], "acc": [], "eval": [], "eval_acc": [], "best": -1}

    with open(config["model_path"] + "/config.json", "w") as fp:
        json.dump(config, fp)
    with open(config["model_path"] + "/w2i.json", "w") as fp:
        json.dump(data["word_to_idx"], fp)

    for I in range(config["num_epochs"]):
        loss, acc = train_epoch(model=model, data=data, config=config)
        eval_loss, eval_acc = eval_epoch(model=model, data=data, config=config)

        metrics["loss"].append(loss)
        metrics["acc"].append(acc)
        metrics["eval"].append(eval_loss)
        metrics["eval_acc"].append(eval_acc)

        if eval_acc > metrics["best"]:
            metrics["best"] = eval_acc
            torch.save(model, config["model_path"] + "/model")

        print(f"{I}\t{loss:.5f}\t{acc:.2f}\t{eval_loss:.5f}\t{eval_acc:.2f}\t{metrics['best']:.2f}")

    with open(config["model_path"] + "/metrics.json", "w") as fp:
        json.dump(metrics, fp)

    # torch.save(model, "./models/" + params["model_name"] + "/model")
    # save_obj(params, "params")


