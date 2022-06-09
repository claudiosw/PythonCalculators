from src.controllers.run_third_calculator_controller import RunThirdCalculatorController
from src.models.http_types.http_request import HttpRequest
import pytest
import json


@pytest.mark.parametrize("input, expected_result", [
    ('{"list_real_numbers": [1, 3, 6]}', True),
    ('{"list_real_numbers": [12, 13, 14]}', False)
])
def test_run_third_calculator_controller(input, expected_result):
    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_third_calculator_controller = RunThirdCalculatorController()
    result = run_third_calculator_controller.run(http_request)

    assert isinstance(result['result'], bool)
    assert result['result'] == expected_result


@pytest.mark.parametrize("input, expected_result", [
    ('{"list_real_numbers": [12, 13, "a"]}', False),
    ('{"list_real_numbers": [12, 13, ""]}', False)
])
def test_run_third_calculator_controller_error(input, expected_result):
    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_third_calculator_controller = RunThirdCalculatorController()
    result = run_third_calculator_controller.run(http_request)

    assert result['error'] == "At least one input is not a real number"
