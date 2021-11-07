import json


class TestConfigurations:

    def __init__(self, max_configs, test_epochs, used_data_paths, training_configurations):
        self.max_configs = max_configs
        self.test_epochs = test_epochs
        self.used_data_paths = used_data_paths
        self.training_configurations = training_configurations

    def get_used_data_paths(self):
        return self.used_data_paths["train"], self.used_data_paths["fine_train"], self.used_data_paths["test"]

    @staticmethod
    def get_training_configuration(training_config):
        return training_config["hidden_neurons"], training_config["learning_rate"], \
               training_config["train_epochs"], training_config["fine_train_epochs"]

    @staticmethod
    def load(path):
        max_configs, used_test_config_path, used_data_paths, data_paths = \
            TestConfigurations._load_test_environment_configuration(path)
        used_data_paths = TestConfigurations._load_used_data_paths(used_data_paths, data_paths)
        test_epochs, training_configurations = TestConfigurations._load_used_test_config(used_test_config_path)

        return TestConfigurations(max_configs, test_epochs, used_data_paths, training_configurations)

    @staticmethod
    def _load_test_environment_configuration(path):
        data = TestConfigurations._load_configuration(path)
        return data["max_configs"], data["used_test_config_path"], data["used_data_paths"], data["data_paths"]

    @staticmethod
    def _load_used_test_config(path):
        data = TestConfigurations._load_configuration(path)
        return data["test_epochs"], data["training_configurations"]

    @staticmethod
    def _load_configuration(path):
        with open(path) as f:
            data = json.load(f)
        return data

    @staticmethod
    def _load_used_data_paths(used_data_paths, data_paths):
        for item in used_data_paths.keys():
            data_path_keys = used_data_paths[item]
            used_data_paths[item] = [data_paths[data_path_key] for data_path_key in data_path_keys]
        return used_data_paths
