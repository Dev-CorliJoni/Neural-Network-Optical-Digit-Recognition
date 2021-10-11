from ai_highscore.custom_exceptions import ConfigurationCollectionMergeError


def test_merge_func():
    pass


def merge(configuration_collections):
    return _merge([[cc, False] for cc in configuration_collections])


def _merge(configuration_collections_data):
    result = []
    for counter, cc_data1 in enumerate(configuration_collections_data[:-1]):
        for cc_data2 in configuration_collections_data[counter + 1:]:
            try:
                result = _get_merged(cc_data1, cc_data2)
                cc_data1[0] = result
            except ConfigurationCollectionMergeError:
                pass


def _get_merged(cc_data1, cc_data2):
    if not cc_data1[1] and not cc_data2[1]:
        merged_cc = cc_data1[0] + cc_data2[0]
        cc_data2[1] = True
        return merged_cc
