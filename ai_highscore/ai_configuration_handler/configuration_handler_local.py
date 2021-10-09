from ai_highscore.models import ConfigurationCollection, Configuration


class ConfigurationHandlerLocal:

    def __init__(self, file_path_list: list):
        self._configurations = ConfigurationCollection(file_path_list)

    def append(self, accuracy, train_epochs, nn):
        i_nodes, h_nodes, o_nodes, learning_rate, weights_ih, weights_ho = nn.get_configuration_data()  # not written function

        self.append(Configuration(i_nodes, h_nodes, o_nodes, learning_rate, train_epochs, weights_ih, weights_ho,
                                  accuracy))

    def append(self, accuracy, input_neurons, hidden_neurons, output_neurons, learning_rate, train_epochs, wih, who):
        self.append(Configuration(input_neurons, hidden_neurons, output_neurons, learning_rate, train_epochs, wih, who,
                                  accuracy))

    def append(self, config):
        self._configurations.append(config)

    def get_configuration_collection(self):
        return self._configurations.sort()
