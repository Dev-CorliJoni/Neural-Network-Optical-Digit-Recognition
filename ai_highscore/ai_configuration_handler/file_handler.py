from ai_highscore.models import Configuration, ConfigurationCollection
import os


class FileHandler:

    @staticmethod
    def load_configs(config_dir):
        configs_collections = []

        for filepath, filename in FileHandler._get_info_about_all_contained_files(config_dir):
            configs_collections.append(FileHandler._load_config(filepath, filename))

        return configs_collections

    @staticmethod
    def _get_info_about_all_contained_files(dir_):
        # All files || dirs of a given dir are collected and transformed
        # to a tuple with the following content(path, name)
        dir_contents = [(os.path.join(dir_, name), name) for name in os.listdir(dir_)]

        # the dirs are filtered from the dir_contents list. It should only contains files afterwards
        return [content for content in dir_contents if not os.path.isdir(content[0])]

    @staticmethod
    def _load_config(path, name):
        config_collection = ConfigurationCollection.create_by_str(str(name))

        with open(path, 'r') as file:
            for line in file:
                if line != "":
                    config = Configuration.create_from_text(line[:-1].split(';;;'))  # line[:-1] to remove \n
                    config_collection.append(config)

        return config_collection.sort()

    @staticmethod
    def save_configs(config_dir, config_collections):
        for config_collection in config_collections:
            name, _, configs = config_collection.resolve()
            path_to_file = os.path.join(config_dir, f"{name}.txt")
            FileHandler._save_config(path_to_file, configs)

    @staticmethod
    def _save_config(path, configs):
        with open(path, 'w') as file:
            file.writelines([conf.to_csv_one_line() for conf in configs])
