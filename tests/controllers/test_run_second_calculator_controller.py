from src.controllers.run_second_calculator_controller import RunSecondCalculatorController
import pytest


@pytest.mark.parametrize("list_input_numbers, expected_result", [
    (["1", "3", "6"], 0.05566481034726358)
])
def test_run_second_calculator_controller(list_input_numbers, expected_result):
    calculator_informations = {
        "list_real_numbers": list_input_numbers
    }
    run_second_calculator_controller = RunSecondCalculatorController()
    result = run_second_calculator_controller.run(calculator_informations)

    assert isinstance(result['result'], float)
    assert result['result'] == expected_result


@pytest.mark.parametrize("list_input_numbers, expected_result", [
    (["1", "3", "a"], None),
    (["1", "3", ""], None)
])
def test_run_second_calculator_controller_error(list_input_numbers, expected_result):
    calculator_informations = {
        "list_real_numbers": list_input_numbers
    }
    run_second_calculator_controller = RunSecondCalculatorController()
    result = run_second_calculator_controller.run(calculator_informations)

    assert result['error'] == "At least one input is not a real number"
