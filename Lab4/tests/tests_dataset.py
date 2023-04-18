# author: Jan Kwiatkowski

from model.dataPreparation import preprocess_dataset

X, y = preprocess_dataset()
print("Atrybuty")
print(X)
print("Klasy")
print(y)
