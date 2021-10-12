from ai_highscore.custom_exceptions import ConfigurationCollectionMergeError
from ai_highscore.models import ConfigurationCollection, Configuration


def test_merge_func():
    pathss = [
        ["iukasdfghuoa/saödlofj/lkdsjfk/file-1.txt", "lkdsjfk/file-1.txt", "saödlofj/lkdsjfk/file-1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file-2.txt", "lkdsjfk/file-1.txt", "saödlofj/lkdsjfk/file-1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file-3.txt", "lkdsjfk/file-1.txt", "saödlofj/lkdsjfk/file-1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file-1.txt", "lkdsjfk/file-1.txt", "saödlofj/lkdsjfk/file-1.txt"],
        ["iukasdfghuoa/saödlofj/lkdsjfk/file-7.txt", "lkdsjfk/file-1.txt", "saödlofj/lkdsjfk/file-1.txt"]
    ]

    ccs = [generate_bullshit(paths) for paths in pathss]
    results = merge(ccs)
    pass


def generate_bullshit(paths: list):
    conf_collection = ConfigurationCollection.create_by_list(paths)
    conf_collection.append(Configuration(784, 500, 10, 0.1, 5, None, None, 93.5))
    conf_collection.append(Configuration(784, 500, 10, 0.1, 5, None, None, 90.5))
    conf_collection.append(Configuration(784, 500, 10, 0.1, 5, None, None, 87.3925))
    return conf_collection


def merge(configuration_collections):
    return _merge([[cc, False] for cc in configuration_collections])


def _merge(configuration_collections_data):
    results = []
    for counter, cc_data1 in enumerate(configuration_collections_data[:-1]):
        for cc_data2 in configuration_collections_data[counter + 1:]:
            try:
                result = _get_merged(cc_data1, cc_data2)
                cc_data1[0] = result
            except ConfigurationCollectionMergeError:
                pass
        if not cc_data1[1]:
            results.append(cc_data1[0])
    return results


def _get_merged(cc_data1, cc_data2):
    if not cc_data1[1] and not cc_data2[1]:
        merged_cc = cc_data1[0] + cc_data2[0]
        cc_data2[1] = True
        return merged_cc
