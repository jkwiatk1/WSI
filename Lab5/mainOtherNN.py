import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split

from otherNN import *


def main():
    X,Y = fetch_openml('mnist_784', data_home="data", return_X_y=True)
    X = np.array(X.values / 255)
    Y = pd.get_dummies(Y) #one-hot encoding for softmax output
    Y = Y.to_numpy(dtype=int)
    X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size = 0.15, random_state=1)


    #
    # data_train_X = X_train.T
    # data_val_X = X_val.T



    # normalize training and val sets
    X_train = normalize_pixels(X_train)
    X_val = normalize_pixels(X_val)

    # set network and optimizer parameters
    # layers_dims = [784, 256, 128, 64, 10]
    layers_dims = [784, 128, 10]
    max_iter = 500
    alpha = 0.1

    # train the network
    params = gradient_descent_optimization(X_train, y_train, layers_dims, max_iter, alpha)


if __name__ == '__main__':
    main()
