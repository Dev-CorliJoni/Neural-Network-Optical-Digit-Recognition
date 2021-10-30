from settings import get_test_data_path_small, get_train_data_path_small, \
    get_test_data_path_big, get_train_data_path_big


# processing method is run_tests_multiprocessing or run_tests_multithreading
def run_tests_big(processing_method, training_configurations, test_epochs, fine_train_paths=[]):
    processing_method(test_epochs, training_configurations,
                      [get_test_data_path_big()], [get_train_data_path_big()], fine_train_paths)


def run_tests_small(processing_method, training_configurations, test_epochs, fine_train_paths=[]):
    processing_method(test_epochs, training_configurations,
                      [get_test_data_path_small()], [get_train_data_path_small()], fine_train_paths)
