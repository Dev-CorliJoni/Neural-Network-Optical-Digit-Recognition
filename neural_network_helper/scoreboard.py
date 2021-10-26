import numpy


class Scoreboard:

    def __init__(self):
        self._scoreboard_success = []
        self._scoreboard_accuracy = []

    def successful_query(self):
        self._scoreboard_success.append(1)

    def unsuccessful_query(self):
        self._scoreboard_success.append(0)

    def _get_lap_accuracy(self):
        accuracy = Scoreboard._get_average(self._scoreboard_success) * 100
        del self._scoreboard_success[:]
        return accuracy

    def finish_query_lap(self):
        self._scoreboard_accuracy.append(self._get_lap_accuracy())
        return self._scoreboard_accuracy[-1]

    def get_laps_average_accuracy(self):
        return Scoreboard._get_average(self._scoreboard_accuracy)

    @staticmethod
    def _get_average(array_):
        array_np = numpy.asarray(array_)
        return array_np.sum() / array_np.size
