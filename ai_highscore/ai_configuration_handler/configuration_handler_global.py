from . import FileHandler


class ConfigurationHandlerGlobal:
    _config_collections = []

    @staticmethod
    def load_configs():
        ConfigurationHandlerGlobal._config_collections = FileHandler.load_configs("Data/Highscores")

    @staticmethod
    def save_configs():
        FileHandler.save_configs("Data/Highscores", ConfigurationHandlerGlobal._config_collections)
