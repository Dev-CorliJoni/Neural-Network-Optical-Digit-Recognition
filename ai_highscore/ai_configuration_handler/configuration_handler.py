from ai_highscore.ai_configuration_handler import FileHandler, merge
from settings import get_configuration_folder
from ai_highscore.models import ConfigurationCollection


class ConfigurationHandler:
    _config_collections = []

    @staticmethod
    def load_configs():
        ConfigurationHandler._config_collections = FileHandler.load_configs(get_configuration_folder())

    @staticmethod
    def save_configs():
        ConfigurationHandler._config_collections = [cc.sort() for cc in merge(ConfigurationHandler._config_collections)]
        FileHandler.save_configs(get_configuration_folder(), ConfigurationHandler._config_collections)

    def __init__(self, file_path_list: list):
        self._configurations = ConfigurationCollection.create_by_list(file_path_list)

    def append_config(self, config):
        self._configurations.append(config)

    def finish_handler(self):
        ConfigurationHandler._config_collections.append(self._configurations)
