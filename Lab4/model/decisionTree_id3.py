# author: Jan Kwiatkowski

import numpy as np
from sklearn.base import BaseEstimator, ClassifierMixin

from model.Metrics import Metrics


class Node(object):
    def __init__(self):
        self.predicted_class = None
        self.threshold = None
        self.feature_idx = None
        self.children = []
        self.fname = None

    def is_leaf_node(self):
        return self.predicted_class is not None


class ID3Tree(BaseEstimator, ClassifierMixin):
    def __init__(self, max_depth=100, min_samples_split=2, fnames=None, classnames=None):
        self.root = None
        self.max_depth = max_depth
        self.min_samples_split = min_samples_split
        self.metrics = Metrics()
        self.fnames = fnames
        self.classnames = classnames

    def fit(self, X, y):
        # list of attributes
        A_ids = np.array(list(range(len(X[0, :]))))
        self._build_tree(A_ids, Sx=X, Sy=y, node=None)

    def _build_tree(self, A_ids: np.ndarray, Sx: np.ndarray, Sy: np.ndarray, node: Node, depth=0):
        if not node:
            node = Node()
            if not self.root:
                self.root = node

        uniq_classes_freqs = np.unique(Sy, return_counts=True)

        # warunki zakończenia
        # przekroczenie maksymalnej glebokosci
        if (depth >= self.max_depth or uniq_classes_freqs == 1 or len(A_ids) < self.min_samples_split):
            most_freq_class_idx = np.argmax(uniq_classes_freqs[1])
            node.predicted_class = int(uniq_classes_freqs[0][most_freq_class_idx])
            if self.classnames:
                node.fname = self.classnames[int(node.predicted_class)]
            return node

        # warunki zakończenia
        # czy wszystkie Sy maja ta sama klase
        if len(uniq_classes_freqs[0]) == 1:
            node.predicted_class = int(uniq_classes_freqs[0])
            if self.classnames:
                node.fname = self.classnames[int(node.predicted_class)]
            return node

        # if A jest pusty then
        #     return stwórz liść(label=najczęstsza wartość ytarget)
        if len(A_ids) == 0:
            most_freq_class_idx = np.argmax(uniq_classes_freqs[1])
            node.predicted_class = int(uniq_classes_freqs[0][most_freq_class_idx])
            if self.classnames:
                node.fname = self.classnames[int(node.predicted_class)]
            return node

        igs_A_sampled = [self.metrics.information_gain(Sx=Sx, Sy=Sy, feature_idx=attr_idx) for attr_idx
                         in A_ids]

        # best attribute to split
        best_attr = A_ids[np.argmax(igs_A_sampled)]
        if self.fnames:
            node.fname = self.fnames[best_attr]

        node.feature_idx = best_attr

        Sx_a_best = Sx[:, best_attr]
        best_attr_values = np.unique(Sx_a_best, return_counts=False)

        best_attr_values = np.sort(best_attr_values)

        for v in best_attr_values:

            # wyciaganie numerow indeksow dla danej wartosci atrybutu
            value_mask = self.create_mask(Sx, v, best_attr)

            if len(value_mask) == 0:
                child_node = Node()
                child_node.threshold = v
                # tego atrybutu zbiór wartości jest pusty, tworzymy liść
                most_freq_class_idx = np.argmax(uniq_classes_freqs[1])
                child_node.predicted_class = int(uniq_classes_freqs[0][most_freq_class_idx])
                if self.classnames:
                    child_node.fname = self.classnames[int(child_node.predicted_class)]
                node.children.append(child_node)
            else:
                Sx_new = Sx[value_mask]
                Sy_new = Sy[value_mask]
                A_ids = np.delete(A_ids, np.where(A_ids == best_attr))
                child_node = self._build_tree(Sx=Sx_new, Sy=Sy_new, A_ids=A_ids, node=None, depth=depth + 1)
                child_node.threshold = v
                node.children.append(child_node)
        return node

    def create_mask(self, Sx, val, attr_id):
        '''
        Tworzy maskę z indeksami Sx który ma wartości atrybutu attr_id = val. (Sx(attr_id).val = val)
        :param Sx: zbiór atrybutow i wartości
        :param val: wartość atrybutu
        :param attr_id: id atrybutu
        :return: maska indeksów Sx
        '''
        return [i for i, x in enumerate(Sx[:, attr_id]) if x == val]

    def predict(self, X):
        node = self.root
        return np.array([self._pred(node=node, x=x) for x in X])

    def _pred(self, node: Node, x):
        if node.is_leaf_node():
            return node.predicted_class

        nchild = len(node.children)

        for child in node.children:
            # wartość atrybutu feature_idx dla danego węzła z wartością odpowiadającą temu atrybutowi w wejściowym wierszu x
            if x[node.feature_idx] <= child.threshold:
                return self._pred(child, x)
            else:
                continue
            # W przeciwnym razie (jeśli wartość jest większa niż próg), funkcja _pred() jest wywoływana dla następnego dziecka.
        return self._pred(node.children[nchild - 1], x)
