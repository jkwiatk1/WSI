import csv

import numpy as np
import pandas as pd
import math
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

from networkTests import NeuralNetwork


def save_to_csv(filename, rows):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Learning rate", "accuracy", "error"])
        writer.writerows(rows)
        f.close()


def main():

    X,Y = fetch_openml('mnist_784', data_home="data", return_X_y=True)
    X = np.array(X.values / 255)
    Y = pd.get_dummies(Y) #one-hot encoding for softmax output
    Y = Y.to_numpy(dtype=int)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.15, random_state=1)
    network = NeuralNetwork(layer_sizes=[784, 256, 64, 10])
    # network = NeuralNetwork(layer_sizes=[784, 128, 10])
    learning_rates = [0.4]
    for lr in learning_rates:
        accuracy, error = network.train(x_train,y_train,lr,10, x_test, y_test)

if __name__ == "__main__":
    main()