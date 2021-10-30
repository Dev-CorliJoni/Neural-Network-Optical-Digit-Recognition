from neural_network_helper import run_tests_multithreading, run_tests_multiprocessing, run_tests_big, run_tests_small
from ai_highscore.ai_configuration_handler import ConfigurationHandler
from settings import get_train_data_path_big, get_test_data_path_big, get_own_test_data_path
import json


class Controller:

    def __init__(self):
        self.initialize = _initialize
        self.run_task = _run_test
        self.finalize = _finalize

    def run(self):
        self.initialize()
        self.run_task()
        self.finalize()


def _initialize():
    ConfigurationHandler.load_configs()


def _run():
    with open('Data/TestConfiguration/TestConfigData-HighHNeurons+LowLR+HighTrainE.json') as f:
        test_epochs, training_configurations = json.load(f).values()
    run_tests_big(run_tests_multiprocessing, training_configurations, test_epochs)


def _test_one():
    from neural_network_helper import NeuralNetworkEvaluator
    NeuralNetworkEvaluator() \
        .train_and_query([get_train_data_path_big()], [get_own_test_data_path()], [get_test_data_path_big()],
                         100, 0.7, 7, 2, 2)


def _run_test():
    [add_bullshit(paths) for paths in [
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_1.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_2.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_3.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_1.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_7.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file_1.txt", "lkdsjfk/file_1.txt", "saödlofj/lkdsjfk/file_1.txt"]
    ]]


def add_bullshit(paths: list):
    from ai_highscore.models import ConfigurationCollection, Configuration
    from ai_highscore.ai_configuration_handler import ConfigurationHandler
    conf_collection = ConfigurationCollection.create_by_list(paths)
    wih, who = (_get_weights(784, 100), _get_weights(100, 10))
    conf_collection.append(Configuration(784, 100, 10, 0.1, 5, wih, who, 93.5))
    conf_collection.append(Configuration(784, 100, 10, 0.1, 5, wih, who, 90.5))
    conf_collection.append(Configuration(784, 100, 10, 0.1, 5, wih, who, 87.3925))
    ConfigurationHandler._config_collections.append(conf_collection)


def _get_weights(first_layer_count, second_layer_count):
    import numpy
    return numpy.random.normal(0.0, pow(second_layer_count, -0.5), (second_layer_count, first_layer_count))


def _finalize():
    ConfigurationHandler.save_configs()
