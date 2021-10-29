from ai_highscore.ai_configuration_handler.file_handler import FileHandler
from neural_network_helper import NeuralNetworkEvaluator
from settings import get_configuration_folder
from concurrent.futures import ProcessPoolExecutor
from threading import Thread
from functools import partial
import json


def run_test_parallel(test_epochs, training_configurations, test_paths, train_paths, fine_train_paths=[]):
    train_func = lambda args: train_and_query_parallel(test_epochs, args, test_paths, train_paths, fine_train_paths)

    with ProcessPoolExecutor() as executor:
        x = executor.map(train_func, training_configurations)


def train_and_query_parallel(test_epochs, args, test_paths, train_paths, fine_train_paths):
    hidden_nodes, learning_rate, train_epochs, fine_train_epochs = args.values()
    nne = NeuralNetworkEvaluator()
    nne.train_and_query(hidden_nodes, learning_rate, train_epochs, test_epochs)
