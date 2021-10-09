#from NeuralNetzworkHelper import run_test_with_threads, run_test_parallel
#from AIConfig import AIConfigHandler


class Controller:

    def __init__(self):
        self.initialize = self._initialize
        self.run_task = self._test_ai_config_module
        self.finalize = self._finalize

    def run(self):
        self.initialize()
        self.run_task()
        self.finalize()

    def _initialize(self):
        pass

    def _run(self):
        pass

    def _finalize(self):
        pass


    #Test Methods

    def _test_ai_config_module(self):
        from ai_highscore.models import ConfigurationCollection
        from ai_highscore import Configuration
        conf_collection = ConfigurationCollection(["iukasdfghuoa/saödlofj/lkdsjfk/file-1.txt", "lkdsjfk/file-1.txt",
                                                   "saödlofj/lkdsjfk/file-1.txt"])

        Configuration(784, 500, 10, 0.1, 5, None, None, 93.5)
        conf_collection.append(Configuration(784, 500, 10, 0.1, 5, None, None, 93.5))
        conf_collection.append(Configuration(784, 500, 10, 0.1, 5, None, None, 90.5))
        conf_collection + Configuration(784, 500, 10, 0.1, 5, None, None, 87.3925)

        print(conf_collection)



