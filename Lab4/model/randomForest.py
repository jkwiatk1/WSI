# author: Jan Kwiatkowski

import numpy as np
from scipy import stats
from sklearn.base import BaseEstimator, ClassifierMixin

from decisionTree_id3 import ID3Tree


class RandomForest(BaseEstimator, ClassifierMixin):
    def __init__(self, n_trees=10, max_depth=100, min_samples_split=2):

        # hiperparametry drzewa ID3
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

        # hiperparametry lasu
        self.n_trees = n_trees
        self.trees = []


    def fit(self, X, y):
        # Reset
        if len(self.trees) > 0:
            self.trees = []

        num_built = 0

        while num_built < self.n_trees:
            clf_id3 = ID3Tree(max_depth=self.max_depth, min_samples_split=self.min_samples_split)

            clf_id3.fit(X, y)
            self.trees.append(clf_id3)
            num_built += 1

    def predict(self, X):
        # Predykcja wyznaczana dla kazdego klasyfikatora w lesie
        y = []
        for tree in self.trees:
            y.append(tree.predict(X))

        y = np.swapaxes(y, axis1=0, axis2=1)

        # Glosowanie wiekszosciowe
        predicted_classes = stats.mode(y, axis=1)[0].reshape(-1)

        return predicted_classes
