# author: Jan Kwiatkowski
import unittest

from model.dataPreparation import preprocess_dataset
from model.informationGain import entropy, entropy_counts, information_gain

X, y = preprocess_dataset()

class Test(unittest.TestCase):

    def test_entropy_counts(self):
        dataSet = [1,1,1,2,2,1,1,1,2,2]
        self.assertEquals(entropy(dataSet), 0.5)



if __name__ == '__main__':
    unittest.main()