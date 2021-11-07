from neural_network_helper import run_tests_multithreading, run_tests_multiprocessing, run_tests
from ai_highscore.ai_configuration_handler import ConfigurationHandlerGlobal
from test_configurations import get_train_data_path_big, get_test_data_path_big, get_own_test_data_path, TestConfigurations


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


def _run():
    configuration = TestConfigurations.load('Data/TestConfiguration/AI-Test-Environment-Configuration.json')
    ConfigurationHandlerGlobal.set_max_configs(configuration.max_configs)
    run_tests(run_tests_multiprocessing, configuration)


def _test_one():
    from neural_network_helper import NeuralNetworkEvaluator
    config_handler = NeuralNetworkEvaluator() \
        .train_and_query([get_train_data_path_big()], [get_own_test_data_path()], [get_test_data_path_big()],
                         5, 0.7, 1, 1, 1)
    ConfigurationHandlerGlobal.finish_handler(config_handler)


def _finalize():
    ConfigurationHandlerGlobal.save_configs()
