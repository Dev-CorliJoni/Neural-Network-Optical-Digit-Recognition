from ai_highscore.custom_exceptions import ConfigurationCollectionMergeError


def merge(configuration_collections):
    return _merge([[cc, False] for cc in configuration_collections])


def _merge(configuration_collections_data):
    merged_configuration_collections = []
    counter = -1
    for counter, cc_data1 in enumerate(configuration_collections_data[:-1]):
        for cc_data2 in configuration_collections_data[counter + 1:]:
            try:
                _merge_in_cc1(cc_data1, cc_data2)
            except ConfigurationCollectionMergeError:
                pass
        _add_if_not_merged(merged_configuration_collections, cc_data1)
    if (not configuration_collections_data) is False:  # list isn`t empty
        _add_if_not_merged(merged_configuration_collections, configuration_collections_data[counter + 1])
    return merged_configuration_collections


def _add_if_not_merged(configuration_collection, cc_data):
    if not cc_data[1]:
        configuration_collection.append(cc_data[0])


def _merge_in_cc1(cc_data1, cc_data2):
    if not cc_data1[1] and not cc_data2[1]:
        cc_data1[0] = cc_data1[0] + cc_data2[0]
        cc_data2[1] = True
