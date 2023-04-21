# author: Jan Kwiatkowski
import unittest

from model.dataPreparation import preprocess_dataset

X, y = preprocess_dataset()
print("Atrybuty")
print(X)
print("Klasy")
print(y)


class Test(unittest.TestCase):
    def test_dataset_size(self):
        self.assertEquals(len(X), len(y))
