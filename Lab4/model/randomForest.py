# author: Jan Kwiatkowski

import numpy as np
import pandas as pd
from scipy import stats
from sklearn.base import BaseEstimator, ClassifierMixin

from decisionTree_id3 import ID3Tree


class RandomForest(BaseEstimator, ClassifierMixin):
    def __init__(self, n_trees=10, subsample_size=None, max_depth=10000000,
                 random_state=None, min_samples_split=2):

        # hiperparametry drzewa ID3
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split

        # hiperparametry lasu
        self.subsample_size = subsample_size
        self.random_state = random_state
        self.trees = []

    def sample(self, X, y, random_state):
        n_samples, n_features = X.shape
        indices = np.arange(n_samples)

        if random_state is not None:
            np.random.seed(random_state)

        np.random.shuffle(indices)

        test_size = int(test_size * n_samples)
        test_indices = indices[:test_size]
        train_indices = indices[test_size:]

        X_train, X_test = X[train_indices], X[test_indices]
        y_train, y_test = y[train_indices], y[test_indices]

        return X_train, y_train, X_test, y_test

    def fit(self, X, y):
        '''
        Parametry:
        ----------
        X: Zbior danych trenujacych
        y: klasa
        '''
        # Reset
        if len(self.trees) > 0:
            self.trees = []

        if isinstance(X, pd.core.frame.DataFrame):
            X = X.values

        if isinstance(y, pd.core.series.Series):
            y = y.values

        num_built = 0

        while num_built < self.n_trees:
            clf_id3 = ID3Tree(max_depth=self.max_depth, min_samples_split=self.min_samples_split)

            # Obtain data sample
            _X, _y, X_test, y_test = self.sample(X, y, self.random_state)

            # Train
            clf_id3.fit(_X, _y)
            # Save the classifier
            self.trees.append(clf_id3)

            num_built += 1

            if self.random_state is not None:
                self.random_state += 1

    def predict(self, X):
        # Predykcja wyznaczana dla kazdego klasyfikatora w lesie
        y = []
        for tree in self.trees:
            y.append(tree.predict(X))

        y = np.swapaxes(y, axis1=0, axis2=1)

        # Glosowanie wiekszosciowe
        predicted_classes = stats.mode(y, axis=1)[0].reshape(-1)

        return predicted_classes
