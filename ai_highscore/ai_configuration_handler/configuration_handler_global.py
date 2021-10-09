from . import FileHandler
from settings import get_configuration_folder


class ConfigurationHandlerGlobal:
    _config_collections = []

    @staticmethod
    def load_configs():
        ConfigurationHandlerGlobal._config_collections = FileHandler.load_configs(get_configuration_folder())

    @staticmethod
    def save_configs():
        FileHandler.save_configs(get_configuration_folder(), ConfigurationHandlerGlobal._config_collections)
