import math
import numpy as np


def calculate_sqrt(input: float) -> float:
    return math.sqrt(input)


def calculate_average(list: list[float]) -> float:
    numpy_array = np.array(list)
    return np.average(numpy_array)


def calculate_standard_deviation(list: list[float]) -> float:
    numpy_array = np.array(list)
    return np.std(numpy_array)


def calculate_variance(list: list[float]) -> float:
    numpy_array = np.array(list)
    return np.var(numpy_array)
