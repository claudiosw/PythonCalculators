from src.controllers.run_first_calculator_controller import RunFirstCalculatorController
import pytest

@pytest.mark.parametrize("input_number, expected_result", [
    (3, 1.630860801189084)
])
def test_run_first_calculator_controller(input_number, expected_result):
    calculator_informations = {
        "real_number": input_number
    }
    run_first_calculator_controller = RunFirstCalculatorController()
    assert run_first_calculator_controller.run(calculator_informations)['result'] == expected_result
