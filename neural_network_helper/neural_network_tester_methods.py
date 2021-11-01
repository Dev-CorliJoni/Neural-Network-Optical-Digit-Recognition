from ai_highscore.ai_configuration_handler import ConfigurationHandlerGlobal
from neural_network_helper import NeuralNetworkEvaluator
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def _run_tests(executor_class, test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    params_list = [(args, test_epochs, test_paths, train_paths, fine_train_paths) for args in training_configurations]

    with executor_class() as executor:
        results = executor.map(_run_test, params_list)

    for result in results:
        if isinstance(result, Exception):
            print(result)
        else:
            ConfigurationHandlerGlobal.finish_handler(result)


def _run_test(params):
    args, test_epochs, test_paths, train_paths, fine_train_paths = params
    hidden_nodes, learning_rate, train_epochs, fine_train_epochs = args.values()
    configuration_handler = NeuralNetworkEvaluator().train_and_query(train_paths, fine_train_paths, test_paths,
                                                                     hidden_nodes, learning_rate,
                                                                     train_epochs, fine_train_epochs, test_epochs)
    return configuration_handler


# Multiprocessing
def run_tests_multiprocessing(test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    _run_tests(ProcessPoolExecutor, test_epochs, training_configurations, test_paths, train_paths, fine_train_paths)


# Multithreading
def run_tests_multithreading(test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    _run_tests(ThreadPoolExecutor, test_epochs, training_configurations, test_paths, train_paths, fine_train_paths)
