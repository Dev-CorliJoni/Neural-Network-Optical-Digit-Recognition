from neural_network_helper import NeuralNetworkEvaluator
from concurrent.futures import ProcessPoolExecutor
from threading import Thread


# Multiprocessing
def run_tests_multiprocessing(test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    def partial_run_test_multiprocessing(args):
        _run_test_multiprocessing(test_epochs, args, test_paths, train_paths, fine_train_paths)

    with ProcessPoolExecutor() as executor:
        x = executor.map(partial_run_test_multiprocessing, training_configurations)


def _run_test_multiprocessing(test_epochs, args, test_paths, train_paths, fine_train_paths):
    hidden_nodes, learning_rate, train_epochs, fine_train_epochs = args.values()
    NeuralNetworkEvaluator().train_and_query(train_paths, fine_train_paths, test_paths, hidden_nodes, learning_rate,
                                             train_epochs, fine_train_epochs, test_epochs)


# Multithreading
def run_tests_multithreading(test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    threads = [_run_test_multithreading(test_epochs, args, test_paths, train_paths, fine_train_paths)
               for args in training_configurations]
    [thread.join() for thread in threads]


def _run_test_multithreading(test_epochs, args, test_paths, train_paths, fine_train_paths):
    hidden_nodes, learning_rate, train_epochs, fine_train_epochs = args.values()
    params = (train_paths, fine_train_paths, test_paths, hidden_nodes, learning_rate,
              train_epochs, fine_train_epochs, test_epochs)
    t = Thread(target=NeuralNetworkEvaluator().train_and_query_big, args=params)
    t.start()
    return t
