# public
def get_combined_file_names(file_paths: list):
    link_element = "-"
    return link_element.join(_get_names_from_paths(file_paths))


def get_combined_file_names_readable(file_paths: list):
    link_element = " - "
    return link_element.join(_get_names_from_paths(file_paths))


# private
def _get_names_from_paths(file_paths: list):
    return [_get_name_from_path(path) for path in file_paths]


def _get_name_from_path(file_path: str):
    name_plus_ext = file_path.split('/')[-1]
    name = name_plus_ext.split('.')[0]
    return name
