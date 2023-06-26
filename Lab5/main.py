import csv

import numpy as np
import pandas as pd
import math
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import os
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

from network import NeuralNetwork


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
    accuracies = []
    errors = []
    performance_summary = []
    learning_rates = [0.1, 0.2, 0.3, 0.4]
    plt.figure(1)
    plt.figure(2)
    for lr in learning_rates:
        accuracy, error = network.train(x_train,y_train,lr,1000, x_test, y_test)
        plt.figure(1)
        plt.plot(accuracy, label=lr)
        plt.title("Accuracy metrics")
        plt.legend()
        accuracies.append(accuracy)
        plt.show()
        plt.figure(2)
        plt.plot(error, label=lr)
        plt.title("Error metrics")
        plt.legend()
        plt.show()
        errors.append(error)
        performance_summary.append([lr, accuracy[-1], error[-1]])

    plt.figure(1)
    plt.show()
    plt.figure(2)
    plt.show()
    save_to_csv("docs/results.csv", performance_summary)
if __name__ == "__main__":
    main()