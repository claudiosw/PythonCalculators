from src.views.run_first_calculator_view import RunFirstCalculatorView
from src.controllers.run_first_calculator_controller import RunFirstCalculatorController


def run_first_calculator_process() -> None:
    """ Process that is run when the user chooses the first calculator
        Calls the respectives controllers and views
    """
    run_first_calculator_view = RunFirstCalculatorView()
    run_first_calculator_controller = RunFirstCalculatorController()

    calculator_informations = run_first_calculator_view.run_first_calculator_page()
    result = run_first_calculator_controller.run(calculator_informations)

    if result['success']:
        run_first_calculator_view.run_first_calculator_success(result)
    else:
        run_first_calculator_view.run_first_calculator_fail(result["error"])
