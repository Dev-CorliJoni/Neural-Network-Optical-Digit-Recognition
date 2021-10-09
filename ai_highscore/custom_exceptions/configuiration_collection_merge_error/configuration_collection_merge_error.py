from ai_highscore.custom_exceptions import ConfigurationCollectionMergeErrorType


class ConfigurationCollectionMergeError(Exception):

    def __init__(self, type_: ConfigurationCollectionMergeErrorType, message: str = None):
        super().__init__()
        self.type = type_
        self.message = self._get_message(message)

    @staticmethod
    def _get_message(self, type_: ConfigurationCollectionMergeErrorType, message):
        if message is None:
            return ConfigurationCollectionMergeErrorType.get_message(type_.value)
        else:
            return message

