# author: Jan Kwiatkowski
import unittest
import numpy as np

from model.Metrics import Metrics

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
        data_set_for_atr0_val0 = [0, 0, 1, 0, 1, 0]
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

    def test_infGain_MoreAtr(self):
        Sx = np.array(
            [[0, 0, 1, 1], [1, 1, 0, 0], [0, 1, 1, 0], [1, 0, 1, 1], [0, 1, 0, 1], [1, 0, 0, 0], [1, 1, 0, 1],
             [0, 1, 1, 1], [1, 1, 1, 0], [0, 0, 0, 0]])
        Sy = np.array([1, 2, 1, 2, 2, 1, 2, 2, 1, 1])

        # Zysk informacji dla pierwszego atrybutu
        a_idx = 0
        expected_value = 0.029
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 3)
        self.assertAlmostEqual(rounded_value, expected_value, places=3)

        # Zysk informacji dla drugiego atrybutu
        a_idx = 1
        expected_value = 0.125
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 3)
        self.assertAlmostEqual(rounded_value, expected_value, places=3)

        # Zysk informacji dla trzeciego atrybutu
        a_idx = 2
        expected_value = 0.029
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 3)
        self.assertAlmostEqual(rounded_value, expected_value, places=3)

        # Zysk informacji dla czwartego atrybutu
        a_idx = 3
        expected_value = 0.278
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 3)
        self.assertAlmostEqual(rounded_value, expected_value, places=3)

    def test_infGain_MoreVals_MoreClass(self):
        # Przykładowy zestaw danych z wieloma atrybutami i klasami
        Sx = np.array(
            [[1, 2, 3, 4], [1, 1, 2, 4], [2, 3, 4, 4], [1, 2, 2, 4], [2, 2, 3, 4], [3, 2, 2, 4], [1, 2, 2, 3],
             [2, 2, 3, 3], [3, 3, 3, 3], [1, 1, 3, 3]])
        Sy = np.array([1, 2, 1, 2, 3, 1, 2, 2, 3, 1])

        expected_value = 1.522
        rounded_value = round(metrics_test.entropy(Sy), 3)
        self.assertAlmostEqual(rounded_value, expected_value, places=3)

        a_idx = 0
        expected_value = 0.36
        rounded_value = round(metrics_test.information_gain(Sx, Sy, a_idx), 2)
        self.assertAlmostEqual(rounded_value, expected_value, places=2)


if __name__ == '__main__':
    unittest.main()
