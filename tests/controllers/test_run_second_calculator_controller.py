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
    assert run_second_calculator_controller.run(calculator_informations)['result'] == expected_result
