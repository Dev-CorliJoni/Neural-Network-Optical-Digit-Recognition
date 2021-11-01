from ai_highscore.ai_configuration_handler import FileHandler, merge
from settings import get_configuration_folder


class ConfigurationHandlerGlobal:
    _config_collections = []
    _max_configs = 10

    @staticmethod
    def load_configs():
        ConfigurationHandlerGlobal._config_collections = FileHandler.load_configs(get_configuration_folder())

    @staticmethod
    def save_configs():
        amount = ConfigurationHandlerGlobal._max_configs
        config_collections = [cc.get_best(amount) for cc in merge(ConfigurationHandlerGlobal._config_collections)]
        ConfigurationHandlerGlobal._config_collections = config_collections
        FileHandler.save_configs(get_configuration_folder(), ConfigurationHandlerGlobal._config_collections)

    @staticmethod
    def finish_handler(configuration_handler_local):
        configurations = configuration_handler_local.get_configuration_collection()
        ConfigurationHandlerGlobal._config_collections.append(configurations)

    @staticmethod
    def set_max_configs(max_configs):
        ConfigurationHandlerGlobal._max_configs = max_configs
