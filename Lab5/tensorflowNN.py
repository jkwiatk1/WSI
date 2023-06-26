import numpy as np
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import tensorflow as tf

def main():
    X,Y = fetch_openml('mnist_784', data_home="data", return_X_y=True)
    X = np.array(X.values / 255)
    Y = pd.get_dummies(Y) #one-hot encoding for softmax output
    Y = Y.to_numpy(dtype=int)
    x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size = 0.15, random_state=1)

    model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(784,)),
        tf.keras.layers.Dense(128, activation='sigmoid'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    model.compile(
        loss='mean_squared_error',
        metrics=['accuracy'],
    )

    model.fit(
        x_train,
        y_train,
        epochs=1000,
        validation_data=(x_test, y_test)
    )

    model.summary()



if __name__ == "__main__":
    main()