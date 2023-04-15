# author: Jan Kwiatkowski
import unittest
import numpy as np

from model.dataPreparation import preprocess_dataset
from model.informationGain import entropy, information_gain

X, y = preprocess_dataset()

class Test(unittest.TestCase):

    def test_entropy(self):
        dataSet = [0,0,0,0,0,1,1,1,1,1]
        self.assertEquals(entropy(dataSet), 1)


    def test_entropy2(self):
        dataSet = [0,0,0,0,0,0,1,1,1,1,1,1,1,1]
        rounded_value = round(entropy(dataSet),2)
        self.assertEquals(rounded_value, 0.99)

    def test_entropy3(self):
        dataSet = [0,0,0,0,0,0,1,1]
        rounded_value = round(entropy(dataSet),2)
        self.assertEquals(rounded_value, 0.81)

    def test_entropy4(self):
        dataSet = [0,0,0,0,1,1]
        rounded_value = round(entropy(dataSet),2)
        self.assertEquals(rounded_value, 0.92)

    def test_IG(self):
        # Sample input data
        Sx = np.array([[1, 'a'], [2, 'b'], [3, 'a'], [4, 'b'], [5, 'c']])
        Sy = np.array(['yes', 'no', 'no', 'yes', 'no'])
        entropy_S = entropy(Sy)
        a_idx = 1

        # Expected output
        expected_ig = 0.17

        # Calculate actual output
        actual_ig = round(information_gain(Sx, Sy, a_idx, entropy_S),2)
        self.assertEquals(actual_ig,expected_ig)



if __name__ == '__main__':
    unittest.main()