from src.controllers.run_third_calculator_controller import RunThirdCalculatorController
import pytest


@pytest.mark.parametrize("list_input_numbers, expected_result", [
    (["1", "3", "6"], True),
    (["12", "13", "14"], False)
])
def test_run_third_calculator_controller(list_input_numbers, expected_result):
    calculator_informations = {
        "list_real_numbers": list_input_numbers
    }
    run_third_calculator_controller = RunThirdCalculatorController()
    result = run_third_calculator_controller.run(calculator_informations)

    assert isinstance(result['result'], bool)
    assert result['result'] == expected_result


@pytest.mark.parametrize("list_input_numbers, expected_result", [
    (["12", "13", "a"], False),
    (["12", "13", ""], False)
])
def test_run_third_calculator_controller_error(list_input_numbers, expected_result):
    calculator_informations = {
        "list_real_numbers": list_input_numbers
    }
    run_third_calculator_controller = RunThirdCalculatorController()
    result = run_third_calculator_controller.run(calculator_informations)

    assert result['error'] == "At least one input is not a real number"
