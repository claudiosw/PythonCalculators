from src.controllers.run_second_calculator_controller import RunSecondCalculatorController
import pytest


@pytest.mark.parametrize("list_input_numbers, expected_result, success", [
    (["1", "3", "6"], 0.05566481034726358, True),
    (["1", "3", "a"], None, False),
    (["1", "3", ""], None, False)
])
def test_run_second_calculator_controller(list_input_numbers, expected_result, success):
    calculator_informations = {
        "list_real_numbers": list_input_numbers
    }
    run_second_calculator_controller = RunSecondCalculatorController()
    result = run_second_calculator_controller.run(calculator_informations)

    assert result['success'] == success
    if success:
        assert isinstance(result['result'], float)
        assert result['result'] == expected_result
    else:
        assert result['error'] == "At least one input is not a real number"
