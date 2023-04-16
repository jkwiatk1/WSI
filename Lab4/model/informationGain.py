# author: Jan Kwiatkowski

import math

import numpy as np

class Metrics:
    def entropy(self, Sy):
        # lista z liczba wystapien obiektow kazdej klasy
        _, Sy_counts = np.unique(Sy, return_counts=True)
        return sum(-count / len(Sy) * math.log2(count / len(Sy)) for count in Sy_counts)

    def entropy_counts(self, Sy, Sy_counts):
        return sum(-count / len(Sy) * math.log2(count / len(Sy)) for count in Sy_counts)

    def information_gain(self, Sx, Sy, a_idx, entropy_S):
        '''
        :param Sx: X podzbiór X
        :param Sy: podzbiór y
        :param a_idx: indeks atrybutu
        :param entropy_S: Entropia dla całego zbioru S
        :return: Information Gain atrybutu a_idx
        '''

        # ilość wystąpień poszczególnych klas w podzbiorze
        _, Sy_counts = np.unique(Sy, return_counts=True)

        # ilość wystąpień poszczególnych wartości atrybutu a_idx w podzbiorze Sx
        Sx_a = Sx[:, a_idx]
        S_a_counts = np.unique(Sx_a, return_counts=True)

        feature_vals = S_a_counts[0]
        feature_vals_freqs = S_a_counts[1] / len(Sx_a)

        feature_vals_mask = [
            [i for i, x in enumerate(Sx_a) if x == y]
            for y in feature_vals
        ]
        result = 0
        for mask, freq in zip(feature_vals_mask, feature_vals_freqs):
            result -= self.entropy(Sy[mask]) * freq

        return entropy_S + result