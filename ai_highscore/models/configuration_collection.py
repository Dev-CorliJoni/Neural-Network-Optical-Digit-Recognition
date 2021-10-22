from ai_highscore.custom_exceptions import ConfigurationCollectionMergeError, ConfigurationCollectionMergeErrorType
from ai_highscore.models import Configuration
from helper.filename_helper import get_combined_file_names, get_combined_file_names_readable, are_combined_names_same


class ConfigurationCollection:
    __configurationCollections = []

    def __init__(self):
        self._ai_configs = []

    # ConfigurationCollections shouldn't have - in their names
    @staticmethod
    def create_by_list(file_path_list: list):
        cc = ConfigurationCollection()
        cc.name = get_combined_file_names(file_path_list)
        cc.name_readable = get_combined_file_names_readable(file_path_list)
        return cc

    @staticmethod
    def create_by_str(file_name: str):
        cc = ConfigurationCollection()
        cc.name = file_name.split('.')[0]
        cc.name_readable = cc.name.replace('-', ' - ')
        return cc

    def append(self, config: Configuration):
        self._ai_configs.append(config)

    def __add__(self, config_collection):
        try:
            if not are_combined_names_same(self.name, config_collection.name):
                raise ConfigurationCollectionMergeError(ConfigurationCollectionMergeErrorType.NAMES_DIFFER)

            self._ai_configs.extend(config_collection.get_collection())
            self._ai_configs = sorted(self._ai_configs, key=lambda c: c.accuracy, reverse=True)

            return self
        except ConfigurationCollectionMergeError as e:
            raise e
        except Exception:
            raise ConfigurationCollectionMergeError(ConfigurationCollectionMergeErrorType.UNKNOWN)

    def get_collection(self):
        return self._ai_configs

    def sort(self):
        self._ai_configs = sorted(self._ai_configs, key=lambda c: c.accuracy, reverse=True)
        return self

    def resolve(self):
        self._ai_configs = sorted(self._ai_configs, key=lambda c: c.accuracy, reverse=True)
        return self.name, self.name_readable, self._ai_configs

    def __str__(self):
        accuracy_string = ", ".join([str(conf.accuracy) for conf in self._ai_configs])
        str_ = f"AI-Configurations | (Training & Test) files:({self.name_readable}) | Accuracies:({accuracy_string})"
        return str_
