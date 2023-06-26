import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def softmax(x):
    exp_x = np.exp(x)
    return exp_x / np.sum(exp_x, axis=1, keepdims=True)


class NeuralNetwork:
    def __init__(self, layer_sizes):
        self.layer_sizes = layer_sizes
        self.num_layers = len(layer_sizes)
        self.weights = []
        self.biases = []
        for i in range(1, self.num_layers):
            prev_size = layer_sizes[i-1]
            curr_size = layer_sizes[i]
            self.weights.append(np.random.randn(prev_size, curr_size))
            self.biases.append(np.zeros((1, curr_size)))

    def der_sigmoid(self, x):
        return sigmoid(x) * (1 - sigmoid(x))

    def forward(self, X):
        self.activations = [X]
        self.z_values = []

        for i in range(self.num_layers - 2):
            z = np.dot(self.activations[i], self.weights[i]) + self.biases[i]
            self.z_values.append(z)
            activation = sigmoid(z)
            self.activations.append(activation)

        z_out = np.dot(self.activations[-1], self.weights[-1]) + self.biases[-1]
        self.z_values.append(z_out)
        output_activation = softmax(z_out)
        self.activations.append(output_activation)

        return self.activations[-1]

    def backward(self, X, y, learning_rate):
        m = X.shape[0]
        delta = (self.activations[-1] - y) / m

        d_weights = []
        d_biases = []

        d_weights.append(np.dot(self.activations[-2].T, delta))
        d_biases.append(np.sum(delta, axis=0, keepdims=True))

        for i in range(self.num_layers - 3, -1, -1):
            delta = np.dot(delta, self.weights[i+1].T) * self.der_sigmoid(self.z_values[i])
            d_weights.insert(0, np.dot(self.activations[i].T, delta))
            d_biases.insert(0, np.sum(delta, axis=0))

        for i in range(self.num_layers - 1):
            self.weights[i] -= learning_rate * d_weights[i]
            self.biases[i] -= learning_rate * d_biases[i]

    def train(self, X, y, learning_rate, epochs, X_test, y_test):
        accuracy_scores = []
        error_rates = []
        display_images = False
        for epoch in range(epochs):
            y_pred = self.forward(X)
            self.backward(X, y, learning_rate)
            if epoch == epochs - 1:
                display_images = True
            accuracy, error = self.performance_metrics(X_test, y_test, display_images)
            accuracy_scores.append(accuracy)
            error_rates.append(error)
            print(f"Iteration {epoch}")
            print(f"Accuracy: {accuracy}")
            print(f"Error rate: {error}")

        return accuracy_scores, error_rates

    def performance_metrics(self, X, y, display_images):
        predictions = self.forward(X)
        predicted_labels = np.argmax(predictions, axis=1)
        true_labels = np.argmax(y, axis=1)

        error_output = ((predicted_labels - true_labels) ** 2).mean()
        accuracy = accuracy_score(true_labels, predicted_labels)
        return accuracy, error_output