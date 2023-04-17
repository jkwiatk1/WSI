# author: Jan Kwiatkowski

import math

import numpy as np

class Metrics:
    def entropy(self, Sy):
        _, counts = np.unique(Sy, return_counts=True)
        p = counts / len(Sy)
        return -np.sum(p * np.log2(p))

    def conditional_entropy(self, x, y):
        res = 0
        vals, counts = np.unique(x, return_counts=True)
        for val, count in zip(vals, counts):
            res += count / len(x) * self.entropy(y[x == val])
        return res

    def information_gain(self, x, y, feature_idx):
        H_S = self.entropy(y)
        H_S_X = self.conditional_entropy(x[:, feature_idx], y)
        return H_S - H_S_X
