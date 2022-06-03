from src.controllers.dependencies import calculate_sqrt, calculate_average, calculate_standard_deviation
from src.controllers.dependencies import calculate_variance
import numpy as np
import pytest


@pytest.mark.parametrize("input_number, expected_result", [
    (9, 3),
    (4, 2)
])
def test_calculate_sqrt(input_number, expected_result):
    assert calculate_sqrt(input_number) == expected_result


@pytest.mark.parametrize("input_list, expected_result", [
    ([1, 2, 3], np.average([1, 2, 3])),
    ([1, 3, 6], np.average([1, 3, 6]))
])
def test_calculate_average(input_list, expected_result):
    assert calculate_average(input_list) == expected_result


@pytest.mark.parametrize("input_list, expected_result", [
    ([1, 2, 3], np.std([1, 2, 3])),
    ([1, 3, 6], np.std([1, 3, 6]))
])
def test_calculate_standard_deviation(input_list, expected_result):
    assert calculate_standard_deviation(input_list) == expected_result


@pytest.mark.parametrize("input_list, expected_result", [
    ([1, 2, 3], np.var([1, 2, 3])),
    ([1, 3, 6], np.var([1, 3, 6]))
])
def test_calculate_variance(input_list, expected_result):
    assert calculate_variance(input_list) == expected_result
