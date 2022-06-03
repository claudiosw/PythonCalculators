from src.views.run_second_calculator_view import RunSecondCalculatorView
from src.controllers.run_second_calculator_controller import RunSecondCalculatorController


def run_second_calculator_process() -> None:
    """ Process that is run when the user chooses the second calculator
        Calls the respectives controllers and views
    """
    run_second_calculator_view = RunSecondCalculatorView()
    run_second_calculator_controller = RunSecondCalculatorController()

    calculator_informations = run_second_calculator_view.run_second_calculator_page()
    result = run_second_calculator_controller.run(calculator_informations)

    if result['success']:
        run_second_calculator_view.run_second_calculator_success(result)
    else:
        run_second_calculator_view.run_second_calculator_fail(result["error"])
