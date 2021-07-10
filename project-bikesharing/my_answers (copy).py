import math

import numpy as np


class NeuralNetwork(object):
    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # Set number of nodes in input, hidden and output layers.
        self.input_nodes = input_nodes
        self.hidden_nodes = hidden_nodes
        self.output_nodes = output_nodes

        # Initialize weights
        self.weights_input_to_hidden = np.random.normal(0.0, self.input_nodes**-0.5,
                                       (self.input_nodes, self.hidden_nodes))

        self.weights_hidden_to_output = np.random.normal(0.0, self.hidden_nodes**-0.5,
                                       (self.hidden_nodes, self.output_nodes))
        self.lr = learning_rate

        #### TODO: Set self.activation_function to your implemented sigmoid function ####
        #
        # Note: in Python, you can define a function with a lambda expression,
        # as shown below.
        self.activation_function = lambda x: 1/(1+np.exp(-x))  # Replace 0 with your sigmoid calculation.

        ### If the lambda code above is not something you're familiar with,
        # You can uncomment out the following three lines and put your
        # implementation there instead.
        #
        #def sigmoid(x):
        #    return 0  # Replace 0 with your sigmoid calculation here
        #self.activation_function = sigmoid


    def train(self, features, targets):
        ''' Train the network on batch of features and targets.

            Arguments
            ---------

            features: 2D array, each row is one data record, each column is a feature
            targets: 1D array of target values

        '''
        n_records = features.shape[0]
        delta_weights_i_h = np.zeros(self.weights_input_to_hidden.shape)
        delta_weights_h_o = np.zeros(self.weights_hidden_to_output.shape)
        for X, y in zip(features, targets):

            final_outputs, hidden_outputs = self.forward_pass_train(X)  # Implement the forward pass function below
            # Implement the backproagation function below
            delta_weights_i_h, delta_weights_h_o = self.backpropagation(final_outputs, hidden_outputs, X, y,
                                                                        delta_weights_i_h, delta_weights_h_o)
        self.update_weights(delta_weights_i_h, delta_weights_h_o, n_records)


    def forward_pass_train(self, X):
        ''' Implement forward pass here

            Arguments
            ---------
            X: features batch

        '''
        #### Implement the forward pass here ####
        ### Forward pass ###
        # TODO: Hidden layer - Replace these values with your calculations.
        hidden_inputs = np.dot(X, self.weights_input_to_hidden) # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs) # signals from hidden layer

        # TODO: Output layer - Replace these values with your calculations.
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_to_output) # signals into final output layer
        final_outputs = final_inputs # signals from final output layer

        return final_outputs, hidden_outputs

    def backpropagation(self, final_outputs, hidden_outputs, X, y, delta_weights_i_h, delta_weights_h_o):
        ''' Implement backpropagation

            Arguments
            ---------
            final_outputs: output from forward pass
            y: target (i.e. label) batch
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers

        '''
        #### Implement the backward pass here ####
        ### Backward pass ###

        # TODO: Output error - Replace this value with your calculations.
        error = y - final_outputs # Output layer error is the difference between desired target and actual output.

        # TODO: Backpropagated error terms - Replace these values with your calculations.
        # output_error_term = error * final_outputs * (1-final_outputs)
        output_error_term = error

        # TODO: Calculate the hidden layer's contribution to the error
        # hidden_error = np.dot(output_error_term, self.weights_hidden_to_output.T)
        # hidden_error = np.dot(output_error_term.T, self.weights_hidden_to_output)
        # hidden_error = np.dot(output_error_term, self.weights_hidden_to_output)
        # print('START')
        # print(self.weights_hidden_to_output.shape) # (2, 1)
        # print(output_error_term.shape) # (1,)
        # # hidden_error = np.dot(self.weights_hidden_to_output, output_error_term)
        hidden_error = np.dot(output_error_term, self.weights_hidden_to_output.T)
        # print('hidden_error', hidden_error)
        # print('END')

        # hidden_error_term = hidden_error
        hidden_error_term = hidden_error * hidden_outputs * (1-hidden_outputs)

        # TODO: Add Weight step (input to hidden) and Weight step (hidden to output).
        # Weight step (input to hidden)
        delta_weights_i_h = delta_weights_i_h + hidden_error_term * X[:, None]

        # Weight step (hidden to output)
        # print(delta_weights_h_o.shape)
        # print(delta_weights_h_o)
        # print(output_error_term.shape)
        # print(output_error_term)
        # print(hidden_outputs.shape)
        # print(hidden_outputs)
        # print((output_error_term * hidden_outputs).shape)
        # print((output_error_term * hidden_outputs))

        # delta_weights_h_o += hidden_outputs.T * output_error_term
        # print('START ***')
        # print(delta_weights_h_o.shape)
        # print(hidden_outputs.shape)
        # print(output_error_term.shape)
        # print((hidden_outputs * output_error_term).shape)
        # print((delta_weights_h_o + hidden_outputs * output_error_term).shape)
        # print(delta_weights_h_o)
        # print((hidden_outputs * output_error_term).reshape(((hidden_outputs * output_error_term).shape[0], 1)))
        # print((hidden_outputs * output_error_term)[:, None])
        # print(delta_weights_h_o + hidden_outputs * output_error_term)
        # print('END ***')
        delta_weights_h_o = delta_weights_h_o + (hidden_outputs * output_error_term)[:, None]
        return delta_weights_i_h, delta_weights_h_o

    def update_weights(self, delta_weights_i_h, delta_weights_h_o, n_records):
        ''' Update weights on gradient descent step

            Arguments
            ---------
            delta_weights_i_h: change in weights from input to hidden layers
            delta_weights_h_o: change in weights from hidden to output layers
            n_records: number of records

        '''

        # TODO: Update the weights with gradient descent step
        # print('1***', self.weights_hidden_to_output.shape)
        # print('1***', self.lr)
        # print('1***', delta_weights_h_o.shape)
        # print('1***', (self.weights_hidden_to_output * self.lr).shape)
        # print('1***', (self.weights_hidden_to_output * self.lr / n_records).shape)
        #
        # print('2***', self.weights_hidden_to_output)
        # print('2***', self.lr)
        # print('2***', (self.weights_hidden_to_output * self.lr))
        # print('2***', (self.weights_hidden_to_output * self.lr / n_records))

        self.weights_hidden_to_output = self.weights_hidden_to_output + self.lr * delta_weights_h_o / n_records # update hidden-to-output weights with gradient descent step
        # print('1***', self.weights_hidden_to_output.shape)
        self.weights_input_to_hidden = self.weights_input_to_hidden + self.lr * delta_weights_i_h / n_records # update input-to-hidden weights with gradient descent step

    def run(self, features):
        ''' Run a forward pass through the network with input features

            Arguments
            ---------
            features: 1D array of feature values
        '''

        #### Implement the forward pass here ####
        # TODO: Hidden layer - replace these values with the appropriate calculations.
        hidden_inputs = np.dot(features, self.weights_input_to_hidden) # signals into hidden layer
        hidden_outputs = self.activation_function(hidden_inputs) # signals from hidden layer

        # TODO: Output layer - Replace these values with the appropriate calculations.
        final_inputs = np.dot(hidden_outputs, self.weights_hidden_to_output) # signals into final output layer
        final_outputs = final_inputs # signals from final output layer

        return final_outputs


#########################################################
# Set your hyperparameters here
##########################################################
# Didn't work
# iterations = 8000
# learning_rate = 0.07
# hidden_nodes = 30
# output_nodes = 1

# Done extremely well!!!
# iterations = 7000
# learning_rate = 0.5
# hidden_nodes = 10
# output_nodes = 1

# Done extremely well!!! Also, slighly less overfitting! But more mistakes
# iterations = 7000
# learning_rate = 0.3
# hidden_nodes = 10
# output_nodes = 1

# # 4: Many mistakes.
# # Progress: 100.0% ... Training loss: 0.000 ... Validation loss: 8.437
# iterations = 3000
# learning_rate = 0.3
# hidden_nodes = 10
# output_nodes = 1

# # 5: Mostly was 0. Didn't fit well
# # Progress: 100.0% ... Training loss: 4.063 ... Validation loss: 0.000
# iterations = 2000
# learning_rate = 1
# hidden_nodes = 2
# output_nodes = 1

# # 6: Slightly better than #5. Fit it slightly better
# # Progress: 100.0% ... Training loss: 2.071 ... Validation loss: 2.866
# iterations = 5000
# learning_rate = 1
# hidden_nodes = 2
# output_nodes = 1

# 7: Majority predictions are negative. Not good.
# Progress: 100.0% ... Training loss: 2.553 ... Validation loss: 4.140
iterations = 7000
learning_rate = 0.8
hidden_nodes = 3
output_nodes = 1