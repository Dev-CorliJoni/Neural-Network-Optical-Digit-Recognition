from ai_highscore.ai_configuration_handler.file_handler import FileHandler
from neural_network_helper import NeuralNetworkEvaluator
from settings import get_configuration_folder
from concurrent.futures import ProcessPoolExecutor
from threading import Thread
import json


class Controller:

    def __init__(self):
        self.initialize = self._initialize
        self.run_task = self._run
        self.finalize = self._finalize

    def run(self):
        self.initialize()
        self.run_task()
        self.finalize()


def _initialize():
    FileHandler.load_configs(get_configuration_folder())


def _run():
    with open('Data/TestConfigurationData/TestConfigData-HighHNeurons+LowLR+HighTrainE.json') as f:
        data = json.load(f)
        # test_data["test_epochs"]
        # test_data["training_configurations"]

def _finalize():
    FileHandler.save_configs(get_configuration_folder())
