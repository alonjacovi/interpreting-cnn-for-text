import torch
from torch import nn
import torch.nn.functional as F
import numpy as np


class CnnClassifier(nn.Module):
    def __init__(self, ngram_sizes, embedding_dim, num_filters, padding_idx, num_classes, vocab_size):
        super(CnnClassifier, self).__init__()
        # self.ngram_sizes = config["model_ngram_sizes"]
        # self.embedding_dim = config["model_embedding_dim"]
        # self.num_filters = config["model_num_filters"]
        # self.padding_idx = config["padding_idx"]  ###
        # self.num_classes = config["num_classes"]  ###
        # self.vocab_size = config["vocab_size"]  ###
        self.ngram_sizes = ngram_sizes
        self.embedding_dim = embedding_dim
        self.num_filters = num_filters
        self.padding_idx = padding_idx
        self.num_classes = num_classes
        self.vocab_size = vocab_size

        self.pad = torch.nn.ConstantPad1d(max(self.ngram_sizes) - 1, self.padding_idx)
        self.embedding = nn.Embedding(self.vocab_size, self.embedding_dim, padding_idx=self.padding_idx)
        self.convs = nn.ModuleList(
            [nn.Conv1d(1, self.num_filters, self.embedding_dim * window_size, stride=self.embedding_dim, bias=True)
             for window_size in self.ngram_sizes]
        )
        self.fc = nn.Linear(self.num_filters * len(self.ngram_sizes), self.num_classes)

    def set_pretrained_embeddings(self, emb, trainable=True):
        self.embedding.weight.data.copy_(torch.from_numpy(emb))
        if not trainable:
            self.embedding.weight.requires_grad = False

    def forward(self, x, thresh_l=None):
        out = {} 

        x = self.pad(x)
        embedded_x = self.embedding(x)
        embedded_x = embedded_x.view(-1, 1, x.shape[1] * embedded_x.shape[2])  # [batch_size, 1, seq_len * word_dim]
        features = [conv(embedded_x) for conv in self.convs]  # [batch_size, num_features, seq_len]
        out['activations_filters'] = features

        features = [F.relu(v) for v in features]
        out['ngram_indices'] = [feat.max(2)[1] for feat in features]

        pooled = [F.max_pool1d(feat, feat.size()[2]).view(-1, feat.shape[1]) for feat in features]
        out['activations_filters_pooled'] = pooled

        if thresh_l is not None:
            for layer, thresh in zip(pooled, thresh_l):
                layer[layer <= thresh] = 0.

        pooled = torch.cat(pooled, 1)
        logit = self.fc(pooled)
        out['logits'] = logit
        return out

    # def forward_log_activations(self, x):
    #     x = self.pad(x)
    #     embedded_x = self.embedding(x)
    #     embedded_x = embedded_x.view(-1, 1, x.shape[1] * embedded_x.shape[2])  # [batch_size, 1, seq_len * word_dim]
    #     features = [conv(embedded_x) for conv in self.convs]
    #     features_act = [F.relu(v) for v in features]  # [batch_size, num_features, seq_len]
    #     ngram_indices = [feat.max(2)[1] for feat in features_act]
    #     pooled = [F.max_pool1d(feat, feat.size()[2]).view(-1, feat.shape[1]) for feat in features_act]
    #     pooled_cat = torch.cat(pooled, 1)
    #     logit = self.fc(pooled_cat)
    #     return logit, features, pooled, ngram_indices

    def get_filters(self):
        return [(conv.weight.squeeze(), conv.bias) for conv in self.convs]

    def get_embeddings(self):
        return self.embedding.weight

    def get_fc_weights(self):
        return self.fc.weight.data, self.fc.bias.data
