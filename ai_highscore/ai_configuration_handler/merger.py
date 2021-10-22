from ai_highscore.custom_exceptions import ConfigurationCollectionMergeError


def merge(configuration_collections):
    return _merge([[cc, False] for cc in configuration_collections])


def _merge(configuration_collections_data):
    results = []
    for counter, cc_data1 in enumerate(configuration_collections_data[:-1]):
        for cc_data2 in configuration_collections_data[counter + 1:]:
            try:
                merge_in_cc1(cc_data1, cc_data2)
            except ConfigurationCollectionMergeError:
                pass
        if not cc_data1[1]:
            results.append(cc_data1[0])
    return results


def merge_in_cc1(cc_data1, cc_data2):
    if not cc_data1[1] and not cc_data2[1]:
        cc_data1[0] = cc_data1[0] + cc_data2[0]
        cc_data2[1] = True
