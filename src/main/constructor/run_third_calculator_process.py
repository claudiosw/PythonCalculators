from src.views.run_third_calculator_view import RunThirdCalculatorView
from src.controllers.run_third_calculator_controller import RunThirdCalculatorController


def run_third_calculator_process() -> None:
    run_third_calculator_view = RunThirdCalculatorView()
    run_third_calculator_controller = RunThirdCalculatorController()

    calculator_informations = run_third_calculator_view.run_third_calculator_page()
    result = run_third_calculator_controller.run(calculator_informations)

    if result['success']:
        run_third_calculator_view.run_third_calculator_success(result)
    else:
        run_third_calculator_view.run_third_calculator_fail(result["error"])
