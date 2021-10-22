# public
def are_combined_names_same(combined_names_1, combined_names_2):
    return _are_combined_names_same(combined_names_1, combined_names_2, "-")


def are_combined_readable_names_same(combined_names_1, combined_names_2):
    return _are_combined_names_same(combined_names_1, combined_names_2, " - ")


# private
# Can be faulty if splitter is contained by single filenames
def _are_combined_names_same(combined_names_as_str_1: str, combined_names_as_str_2: str, splitter, first=True):
    result = _are_name_list_elements_in_combined_names_str(
        combined_names_as_str_1,
        combined_names_as_str_2.split(splitter))

    if not result:
        return False
    elif first:
        return _are_combined_names_same(combined_names_as_str_2, combined_names_as_str_1, splitter, False)
    else:
        return True


def _are_name_list_elements_in_combined_names_str(combined_names_str: str, name_list: list):
    if not combined_names_str and not name_list:
        return False

    for filename in name_list:
        if filename not in combined_names_str:
            return False

    return True
