from enum import Enum


class ConfigurationCollectionMergeErrorType(Enum):
    UNKNOWN = 0
    NAMES_DIFFER = 1

    __type_message_link = {
        {0, "Unknown Error has occurred"},
        {1, "Error has been occurred because the names of the ConfigurationCollections are different"}
    }

    @staticmethod
    def get_message(digit: int):
        return ConfigurationCollectionMergeErrorType.__type_message_link[digit]


