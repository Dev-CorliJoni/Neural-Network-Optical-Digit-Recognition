# from NeuralNetzworkHelper import run_test_with_threads, run_test_parallel
# from AIConfig import AIConfigHandler


class Controller:

    def __init__(self):
        self.initialize = self._initialize
        self.run_task = self._run
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
