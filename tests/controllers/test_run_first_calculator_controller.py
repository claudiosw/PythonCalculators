from src.controllers.run_first_calculator_controller import RunFirstCalculatorController
import pytest


@pytest.mark.parametrize("input_number, expected_result, success", [
    ('3', 1.630860801189084, True),
    ('a', None, False),
    ('', None, False)
])
def test_run_first_calculator_controller(input_number, expected_result, success):
    calculator_informations = {
        "real_number": input_number
    }
    run_first_calculator_controller = RunFirstCalculatorController()
    result = run_first_calculator_controller.run(calculator_informations)

    assert result['success'] == success
    if success:
        assert isinstance(result['result'], float)
        assert result['result'] == expected_result
    else:
        assert result['error'] == "Input is not a real number"
