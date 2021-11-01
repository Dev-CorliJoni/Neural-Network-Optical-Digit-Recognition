from ai_highscore.models import ConfigurationCollection


class ConfigurationHandlerLocal:
    def __init__(self, file_path_list: list):
        self._configurations = ConfigurationCollection.create_by_list(file_path_list)

    def append_config(self, config):
        self._configurations.append(config)

    def get_configuration_collection(self):
        return self._configurations
