from scipy.special import expit, logit
import numpy


class NeuralNetwork:

    def __init__(self, input_nodes, hidden_nodes, output_nodes, learning_rate):
        # inits learning
        self._learning_rate = learning_rate

        # inits the layers
        self._input_nodes = input_nodes
        self._hidden_nodes = hidden_nodes
        self._output_nodes = output_nodes

        # inits the weights
        self._weights_input_hidden = NeuralNetwork._get_weights(self._input_nodes, self._hidden_nodes)
        self._weights_hidden_output = NeuralNetwork._get_weights(self._hidden_nodes, self._output_nodes)

    @staticmethod
    def _get_weights(first_layer_count, second_layer_count):
        return numpy.random.normal(0.0, pow(second_layer_count, -0.5), (second_layer_count, first_layer_count))

    # Trains the Neural Network
    def train(self, inputs_list, targets_list):
        final_outputs, hidden_outputs, inputs = self.query(inputs_list)
        output_errors, hidden_errors = self._get_errors(targets_list, final_outputs)

        # Updates the weights
        self._weights_hidden_output += self._get_weights_adjustments(hidden_outputs, final_outputs, output_errors)
        self._weights_input_hidden += self._get_weights_adjustments(inputs, hidden_outputs, hidden_errors)

    # Calculates the errors for each layer
    def _get_errors(self, targets_list, final_outputs):
        output_errors = NeuralNetwork._convert_list_to_2d_array(targets_list) - final_outputs
        hidden_errors = numpy.dot(self._weights_hidden_output.T, output_errors)
        return output_errors, hidden_errors

    def _get_weights_adjustments(self, inputs, outputs, errors):
        return self._learning_rate * numpy.dot((errors * outputs * (1.0 - outputs)), numpy.transpose(inputs))

    # Query the Neural Network
    def query(self, inputs_list):
        inputs = NeuralNetwork._convert_list_to_2d_array(inputs_list)

        hidden_nodes_output = NeuralNetwork._query_next_node(self._weights_input_hidden, inputs)
        final_nodes_output = NeuralNetwork._query_next_node(self._weights_hidden_output, hidden_nodes_output)

        return final_nodes_output, hidden_nodes_output, inputs

    @staticmethod
    def _query_next_node(weights, last_outputs):
        # calculates the inputs of the next node
        # Multiplies last_outputs with the weights between this and the next node
        next_nodes_input = numpy.dot(weights, last_outputs)
        # calculates the output of the next node (Applies Activation Function)
        next_nodes_output = NeuralNetwork._activation_function(next_nodes_input)
        return next_nodes_output

    def query_reversed(self, targets_list):
        final_outputs = NeuralNetwork._convert_list_to_2d_array(targets_list)

        hidden_outputs = NeuralNetwork._query_next_node_reversed(final_outputs, self._weights_hidden_output)
        inputs = NeuralNetwork._query_next_node_reversed(hidden_outputs, self._weights_input_hidden)

        return inputs

    @staticmethod
    def _query_next_node_reversed(output, weights):
        # calculates the input from the output with the inverse activation function
        _right_input = NeuralNetwork.inverse_activation_function(output)

        # calculate the signal out of the input layer
        left_output = numpy.dot(weights, _right_input)
        # scale them back to 0.01 to .99
        left_output -= numpy.min(left_output)
        left_output /= numpy.max(left_output)
        left_output *= 0.98
        left_output += 0.01

        return left_output

    # Convert list to 2d array
    @staticmethod
    def _convert_list_to_2d_array(list_):
        return numpy.array(list_, ndmin=2).T

    # Applies activation function(sigmoid function)
    @staticmethod
    def _activation_function(x):
        return expit(x)

    # Applies inverse activation function(logit function)
    @staticmethod
    def _inverse_activation_function(x):
        return logit(x)

    def __str__(self):
        return f"|Neural Network -> Input Nodes: {self._input_nodes} - Hidden Nodes: {self._hidden_nodes} - Output " \
               f"Nodes: {self._output_nodes} - Learning Rate: {self._learning_rate}| "

    def get_configuration_data(self):
        return (self._input_nodes, self._hidden_nodes, self._output_nodes, self._learning_rate,
                self._weights_input_hidden, self._weights_hidden_output)
