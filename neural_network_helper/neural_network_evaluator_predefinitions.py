from settings import get_test_data_path_small, get_train_data_path_small, \
    get_test_data_path_big, get_train_data_path_big


def train_and_query_big_once(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs):
    train_and_query_big(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs, 1)


def train_and_query_small_once(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs):
    train_and_query_small(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs, 1)


def train_and_query_big(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs, test_epochs):
    neural_network_evaluator.train_and_query([get_train_data_path_big()],
                                             [get_test_data_path_big()],
                                             hidden_nodes, learning_rate, train_epochs, test_epochs)


def train_and_query_small(neural_network_evaluator, hidden_nodes, learning_rate, train_epochs, test_epochs):
    neural_network_evaluator.train_and_query([get_train_data_path_small()],
                                             [get_test_data_path_small()],
                                             hidden_nodes, learning_rate, train_epochs, test_epochs)
