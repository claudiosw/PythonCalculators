""" In this file we have math functions that use external libraries.
    In other words, all uses of math external libraries should be in this file
"""
import math
import numpy as np


def calculate_sqrt(input: float) -> float:
    """ Calculate square root
        :param  - input: float number parameter
        :return - Square root of the input
    """
    return math.sqrt(input)


def calculate_average(list: list[float]) -> float:
    """ Calculate the average of the numbers of the input list
        :param  - list: list of float numbers
        :return - Average of the numbers of the list
    """
    numpy_array = np.array(list)
    return np.average(numpy_array)


def calculate_standard_deviation(list: list[float]) -> float:
    """ Calculate the standard deviation of the numbers of the input list
        :param  - list: list of float numbers
        :return - Standard deviation of the numbers of the list
    """
    numpy_array = np.array(list)
    return np.std(numpy_array)


def calculate_variance(list: list[float]) -> float:
    """ Calculate the variance of the numbers of the input list
        :param  - list: list of float numbers
        :return - Variance of the numbers of the list
    """
    numpy_array = np.array(list)
    return np.var(numpy_array)
