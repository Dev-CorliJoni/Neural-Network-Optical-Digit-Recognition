from ai_highscore.custom_exceptions.configuiration_collection_merge_error import ConfigurationCollectionMergeErrorType,\
    get_message


class ConfigurationCollectionMergeError(Exception):

    def __init__(self, type_: ConfigurationCollectionMergeErrorType, message: str = None):
        super().__init__()
        self.type = type_
        self.message = self._get_message(type_, message)

    @staticmethod
    def _get_message(type_: ConfigurationCollectionMergeErrorType, message):
        if message is None:
            return get_message(type_.value)
        else:
            return message
