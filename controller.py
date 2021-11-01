from neural_network_helper import run_tests_multithreading, run_tests_multiprocessing, run_tests_big, run_tests_small
from ai_highscore.ai_configuration_handler import ConfigurationHandlerGlobal
from settings import get_train_data_path_big, get_test_data_path_big, get_own_test_data_path
import json


class Controller:

    def __init__(self):
        self.initialize = _initialize
        self.run_task = _run
        self.finalize = _finalize

    def run(self):
        self.initialize()
        self.run_task()
        self.finalize()


def _initialize():
    ConfigurationHandlerGlobal.load_configs()
    ConfigurationHandlerGlobal.set_max_configs(10)


def _run():
    with open('Data/TestConfiguration/TestConfigData-HighHNeurons+LowLR+HighTrainE.json') as f:
        test_epochs, training_configurations = json.load(f).values()
    run_tests_big(run_tests_multiprocessing, training_configurations, test_epochs)


def _test_one():
    from neural_network_helper import NeuralNetworkEvaluator
    config_handler = NeuralNetworkEvaluator() \
        .train_and_query([get_train_data_path_big()], [get_own_test_data_path()], [get_test_data_path_big()],
                         5, 0.7, 1, 1, 1)
    ConfigurationHandlerGlobal.finish_handler(config_handler)


def _finalize():
    ConfigurationHandlerGlobal.save_configs()
