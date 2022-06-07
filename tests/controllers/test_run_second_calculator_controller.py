from src.controllers.run_second_calculator_controller import RunSecondCalculatorController
from src.models.http_types.http_request import HttpRequest
import pytest
import json


@pytest.mark.parametrize("input, expected_result", [
    ('{"list_real_numbers": [1, 3, 6]}', 0.05566481034726358)
])
def test_run_second_calculator_controller(input, expected_result):
    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_second_calculator_controller = RunSecondCalculatorController()
    result = run_second_calculator_controller.run(http_request)

    assert result["success"] is True
    assert isinstance(result['result'], float)
    assert result['result'] == expected_result


@pytest.mark.parametrize("input, expected_result", [
    ('{"list_real_numbers": [1, 3, "a"]}', None),
    ('{"list_real_numbers": [1, 3, ""]}', None)
])
def test_run_second_calculator_controller_error(input, expected_result):

    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_second_calculator_controller = RunSecondCalculatorController()
    result = run_second_calculator_controller.run(http_request)

    assert result['error'] == "At least one input is not a real number"
