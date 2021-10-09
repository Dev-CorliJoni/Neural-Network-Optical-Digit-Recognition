import numpy


def bytes_to_numpy_float64_array(bytes_, shape):
    return numpy.frombuffer(bytes_, numpy.float64).reshape(shape)
