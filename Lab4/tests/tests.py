# author: Jan Kwiatkowski
import unittest
import numpy as np

from model.dataPreparation import preprocess_dataset
from model.Metrics import Metrics, Metrics2

X, y = preprocess_dataset()
metrics_test = Metrics()
metrics_test2 = Metrics2()


class Test(unittest.TestCase):

    def test_entropy(self):
        dataSet = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        self.assertEquals(metrics_test.entropy(dataSet), 1)

    def test_entropy2(self):
        dataSet = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
        rounded_value = round(metrics_test.entropy(dataSet), 2)
        self.assertEquals(rounded_value, 0.99)

    def test_entropy3(self):
        dataSet = [0, 0, 0, 0, 0, 0, 1, 1]
        rounded_value = round(metrics_test.entropy(dataSet), 2)
        self.assertEquals(rounded_value, 0.81)

    def test_entropy4(self):
        dataSet = [0, 0, 0, 0, 1, 1]
        rounded_value = round(metrics_test.entropy(dataSet), 2)
        self.assertEquals(rounded_value, 0.92)

    def test_InfGain(self):
        Sx = np.array([[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [1, 1], [1, 2], [1, 3], [2, 2], [2, 3]])
        Sy = np.array([0, 0, 0, 0, 0, 1, 1, 1, 1, 1])
        a_idx = 1
        entropy_S = metrics_test.entropy(Sy)
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx, entropy_S), 2)
        self.assertEquals(rounded_value, 0.05)


    def test_InfGain2(self):
        Sx = np.array(
            [[1, 1], [2, 2], [2, 2], [2, 1], [2, 2], [1, 2], [2, 1], [2, 1], [1, 2], [2, 2], [1, 2], [1, 2], [1, 2],
             [2, 2]])
        Sy = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        a_idx = 1
        entropy_S = metrics_test.entropy(Sy)
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx, entropy_S), 2)
        self.assertEquals(rounded_value, 0.04)

    def test_InfGain3(self):
        Sx = np.array(
            [[1, 1], [2, 2], [2, 2], [2, 1], [2, 2], [1, 2], [2, 1], [2, 1], [1, 2], [2, 2], [1, 2], [1, 2], [1, 2],
             [2, 2]])
        Sy = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        a_idx = 0
        entropy_S = metrics_test.entropy(Sy)
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx, entropy_S), 2)
        self.assertEquals(rounded_value, 0.13)


    def test_entropyV2(self):
        dataSet = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
        self.assertEquals(metrics_test2.entropy(dataSet), 1)

    def test_entropyV2_2(self):
        dataSet = [0, 0, 0, 0, 0, 0, 1, 1]
        rounded_value = round(metrics_test2.entropy(dataSet), 2)
        self.assertEquals(rounded_value, 0.81)

    def test_InfGainV2(self):
        Sx = np.array(
            [[1, 1], [2, 2], [2, 2], [2, 1], [2, 2], [1, 2], [2, 1], [2, 1], [1, 2], [2, 2], [1, 2], [1, 2], [1, 2],
             [2, 2]])
        Sy = np.array([0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0])
        a_idx = 0
        rounded_value = round(metrics_test2.information_gain(Sx, Sy, a_idx), 2)
        self.assertEquals(rounded_value, 0.13)


if __name__ == '__main__':
    unittest.main()
