# author: Jan Kwiatkowski
import unittest
import numpy as np

from model.dataPreparation import preprocess_dataset
from model.Metrics import Metrics

X, y = preprocess_dataset()
metrics_test = Metrics()


class Test(unittest.TestCase):
    def test_entropy(self):
        dataSet = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        self.assertEquals(metrics_test.entropy(dataSet), 1)

    def test_entropy_2(self):
        data_set_for_all_S = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        rounded_value = round(metrics_test.entropy(data_set_for_all_S), 2)
        self.assertEquals(rounded_value, 0.99)

    def test_entropy_3(self):
        data_set_for_atr0_val1 = [0, 0, 0, 0, 0, 0, 1, 1]
        rounded_value = round(metrics_test.entropy(data_set_for_atr0_val1), 2)
        self.assertEquals(rounded_value, 0.81)

    def test_entropy_4(self):
        data_set_for_atr0_val0 = [0, 0,1, 0,1,0]
        rounded_value = round(metrics_test.entropy(data_set_for_atr0_val0), 2)
        self.assertEquals(rounded_value, 0.92)

    def test_InfGain(self):
        Sx = np.array(
            [[1, 1], [2, 2], [2, 2], [2, 1], [2, 2], [1, 2], [2, 1], [2, 1], [1, 2], [2, 2], [1, 2], [1, 2], [1, 2],
             [2, 2]])
        Sy = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        a_idx = 0
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 2)
        self.assertEquals(rounded_value, 0.13)

    def test_InfGain_2(self):
        Sx = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [1, 1], [1, 2], [1, 3], [2, 2], [2, 3]])
        Sy = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        a_idx = 1
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 2)
        self.assertEquals(rounded_value, 0.05)

    def test_InfGain_3(self):
        Sx = np.array(
            [[1, 1], [2, 2], [2, 2], [2, 1], [2, 2], [1, 2], [2, 1], [2, 1], [1, 2], [2, 2], [1, 2], [1, 2], [1, 2],
             [2, 2]])
        Sy = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        a_idx = 1
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 2)
        self.assertEquals(rounded_value, 0.04)


if __name__ == '__main__':
    unittest.main()
