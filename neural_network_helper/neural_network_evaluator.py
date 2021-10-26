import numpy

from neural_network_helper import Scoreboard
from neural_networks import NeuralNetwork

from ai_highscore.ai_configuration_handler import ConfigurationHandler
from ai_highscore.models import Configuration


class NeuralNetworkEvaluator:

    def __init__(self):
        self.nn = None
        self.scoreboard = None
        self.input_nodes, self.output_nodes = (784, 10)

    def train_and_query(self, train_paths, test_paths, hidden_nodes, learning_rate, train_epochs, test_epochs,
                        save_ai_conf=True):
        print(f"start train and query | Config - Hidden Nodes: {hidden_nodes} | Learning Rate: {learning_rate} | "
              f"Train Epochs: {train_epochs} | Test Epochs: {test_epochs} ")

        self.scoreboard = Scoreboard()
        configuration_handler = ConfigurationHandler(test_paths)

        for _ in range(test_epochs):
            self.nn = NeuralNetwork(self.input_nodes, hidden_nodes, self.output_nodes, learning_rate)
            self.execute_action_with_input(train_paths, self.train_network, train_epochs)
            self.execute_action_with_input(test_paths, self.query_network)
            accuracy = self.scoreboard.finish_query_lap()
            if save_ai_conf:
                config = Configuration.create_from_neural_network(accuracy, train_epochs, self.nn)
                configuration_handler.append_config(config)

        print(f"Config - Hidden Nodes: {hidden_nodes} | Learning Rate: {learning_rate} | Train Epochs: {train_epochs} |"
              f" Average accuracy:{self.scoreboard.get_laps_average_accuracy()}\n\n")

    def execute_action_with_input(self, filepaths, action, epochs=1):
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
