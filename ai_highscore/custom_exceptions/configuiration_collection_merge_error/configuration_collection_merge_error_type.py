from enum import Enum

__type_message_link = {
    0: "Unknown Error has occurred",
    1: "Error has been occurred because the names of the ConfigurationCollections are different"
}


def get_message(digit: int):
    return __type_message_link[digit]


class ConfigurationCollectionMergeErrorType(Enum):
    UNKNOWN = 0
    NAMES_DIFFER = 1
