from src.controllers.dependencies import calculate_sqrt, calculate_average
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
