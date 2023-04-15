# author: Jan Kwiatkowski
import unittest

from model.dataPreparation import preprocess_dataset
from model.informationGain import entropy, entropy_counts, information_gain

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


if __name__ == '__main__':
    unittest.main()