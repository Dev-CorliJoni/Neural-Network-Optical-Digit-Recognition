import time
import numpy

from neural_network_helper import Scoreboard
from neural_networks import NeuralNetwork

from ai_highscore.ai_configuration_handler import ConfigurationHandlerLocal
from ai_highscore.models import Configuration


class NeuralNetworkEvaluator:

    def __init__(self):
        self.nn = None
        self.scoreboard = None
        self.input_nodes, self.output_nodes = (784, 10)

    def train_and_query(self, train_paths, fine_train_paths, test_paths, hidden_nodes, learning_rate,
                        train_epochs, fine_train_epochs, test_epochs, save_config=True):
        self.scoreboard = Scoreboard()
        configuration_handler = ConfigurationHandlerLocal(test_paths)

        NeuralNetworkEvaluator.print_start(hidden_nodes, learning_rate, train_epochs, fine_train_epochs, test_epochs)
        start = time.time()

        for _ in range(test_epochs):
            self.test_lap(train_paths, fine_train_paths, test_paths, hidden_nodes, learning_rate,
                          train_epochs, fine_train_epochs)
            self.process_lap_response(train_epochs, configuration_handler, save_config)

        laps_average_accuracy = self.scoreboard.get_laps_average_accuracy()
        NeuralNetworkEvaluator.print_end(hidden_nodes, learning_rate, train_epochs, laps_average_accuracy, start)
        return configuration_handler

    def test_lap(self, train_paths, fine_train_paths, test_paths, hidden_nodes, learning_rate,
                 train_epochs, fine_train_epochs):
        self.nn = NeuralNetwork(self.input_nodes, hidden_nodes, self.output_nodes, learning_rate)
        NeuralNetworkEvaluator.execute_action(train_paths, self.train_network, train_epochs)
        NeuralNetworkEvaluator.execute_action(fine_train_paths, self.train_network, fine_train_epochs)
        NeuralNetworkEvaluator.execute_action(test_paths, self.query_network)

    def process_lap_response(self, train_epochs, config_handler, save_config):
        accuracy = self.scoreboard.finish_query_lap()
        NeuralNetworkEvaluator.add_config(config_handler, accuracy, train_epochs, self.nn, save_config)

    @staticmethod
    def execute_action(filepaths, action, epochs=1):
        for _ in range(epochs):
            for filepath in filepaths:
                with open(filepath, 'r') as file:
                    for line in file:
                        line_content = line.split(',')

                        # Convert inputs to be between (0.01-0.99)
                        inputs = (numpy.asfarray(line_content[1:]) / 255.0 * 0.99) + 0.01
                        action(int(line_content[0]), inputs)

    def train_network(self, expected, inputs):
        targets = numpy.zeros(self.output_nodes) + 0.01
        targets[expected] = 0.99
        self.nn.train(inputs, targets)

    def query_network(self, expected, inputs):
        outputs, _, _ = self.nn.query(inputs)
        output_digit = numpy.argmax(outputs)

        # If error, is expected a int
        if expected == output_digit:
            self.scoreboard.successful_query()
        else:
            self.scoreboard.unsuccessful_query()

    @staticmethod
    def add_config(configuration_handler, accuracy, train_epochs, neural_network, save_config):
        if save_config:
            config = Configuration.create_from_neural_network(accuracy, train_epochs, neural_network)
            configuration_handler.append_config(config)

    @staticmethod
    def print_start(hidden_nodes, learning_rate, train_epochs, fine_train_epochs, test_epochs):
        print(f"start train and query | Config - Hidden Nodes: {hidden_nodes} | Learning Rate: {learning_rate} | "
              f"Train Epochs: {train_epochs}| Fine-Train Epochs: {fine_train_epochs} | Test Epochs: {test_epochs}\n")

    @staticmethod
    def print_end(hidden_nodes, learning_rate, train_epochs, laps_average_accuracy, start_time):
        print(f"Config - Hidden Nodes: {hidden_nodes} | Learning Rate: {learning_rate} | Train Epochs: {train_epochs} |"
              f" Average accuracy: {laps_average_accuracy}% | Test-execution time: {time.time() - start_time}s\n\n")
