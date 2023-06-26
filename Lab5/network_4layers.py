class NeuralNetwork:
    def __init__(self, input_size, hidden_size1, hidden_size2, output_size):
        self.input_size = input_size
        self.hidden_size1 = hidden_size1
        self.hidden_size2 = hidden_size2
        self.output_size = output_size
        self.weights1 = np.random.randn(self.input_size, self.hidden_size1)
        self.weights2 = np.random.randn(self.hidden_size1, self.hidden_size2)
        self.weights3 = np.random.randn(self.hidden_size2, self.output_size)
        self.biases1 = np.zeros((1, self.hidden_size1))
        self.biases2 = np.zeros((1, self.hidden_size2))
        self.biases3 = np.zeros((1, self.output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def der_sigmoid(self, x):
        return self.sigmoid(x) * (1 - self.sigmoid(x))

    def softmax(self, x):
        exp_x = np.exp(x)
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)

    def forward(self, X):
        self.s1 = np.dot(X, self.weights1) + self.biases1
        self.y1 = self.sigmoid(self.s1)
        self.s2 = np.dot(self.y1, self.weights2) + self.biases2
        self.y2 = self.sigmoid(self.s2)
        self.s3 = np.dot(self.y2, self.weights3) + self.biases3
        self.y3 = self.softmax(self.s3)
        return self.y3

    def backpropagation(self, X, y, learning_rate):
        m = X.shape[0]

        # Output layer
        error_output = (self.y3 - y) / m
        d_biases3 = np.sum(error_output, axis=0, keepdims=True)
        d_weights3 = np.dot(self.y2.T, error_output)

        # Hidden layer 2
        error_hidden2 = np.dot(error_output, self.weights3.T) * self.der_sigmoid(self.y2)
        d_biases2 = np.sum(error_hidden2, axis=0, keepdims=True)
        d_weights2 = np.dot(self.y1.T, error_hidden2)

        # Hidden layer 1
        error_hidden1 = np.dot(error_hidden2, self.weights2.T) * self.der_sigmoid(self.y1)
        d_biases1 = np.sum(error_hidden1, axis=0)
        d_weights1 = np.dot(X.T, error_hidden1)

        # Update weights and biases
        self.weights3 -= learning_rate * d_weights3
        self.biases3 -= learning_rate * d_biases3
        self.weights2 -= learning_rate * d_weights2
        self.biases2 -= learning_rate * d_biases2
        self.weights1 -= learning_rate * d_weights1
        self.biases1 -= learning_rate * d_biases1

    def train(self, X, y, learning_rate, epochs, X_test, y_test):
        accuracy_scores = []
        error_rates = []
        display_images = False
        for epoch in range(epochs):
            a3 = self.forward(X)
            self.backpropagation(X, y, learning_rate)
            if epoch == epochs - 1:
                display_images = True
            accuracy, error = self.performance_metrics(X_test, y_test, display_images)
            accuracy_scores.append(accuracy)
            error_rates.append