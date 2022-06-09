from src.controllers.run_first_calculator_controller import RunFirstCalculatorController
from src.models.http_types.http_request import HttpRequest
import pytest
import json


@pytest.mark.parametrize("input, expected_result", [
    ('{"real_number": 3}', 1.630860801189084)
])
def test_run_first_calculator_controller(input, expected_result):
    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_first_calculator_controller = RunFirstCalculatorController()
    result = run_first_calculator_controller.run(http_request)

    assert result["success"] is True
    assert isinstance(result['result'], float)
    assert result['result'] == expected_result


@pytest.mark.parametrize("input, expected_result", [
    ('{"real_number": "a"}', None),
    ('{"real_number": ""}', None)
])
def test_run_first_calculator_controller_error(input, expected_result):
    http_request = HttpRequest(
        body=json.loads(input)
    )
    run_first_calculator_controller = RunFirstCalculatorController()
    result = run_first_calculator_controller.run(http_request)

    assert result["success"] is False
    assert result["error"] == "Input is not a real number"
