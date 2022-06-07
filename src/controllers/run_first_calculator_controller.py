from typing import Dict
from .dependencies.math_dependencies import calculate_sqrt, calculate_average
from .interfaces.calculators_interface import CalculatorsInterface
from src.models.http_types.http_request import HttpRequest


class RunFirstCalculatorController(CalculatorsInterface):
    """ Class to define first calculator """

    def run(self, http_request: HttpRequest) -> Dict[bool, float]:
        """ Run first calculator
        :param  - http_request: http request
        :return - Dictionary with informations of the process
        """

        try:
            calculator_informations = {"real_number": http_request.body["real_number"]}
            self.__convert_validate(calculator_informations)
            result = self.__calculate(calculator_informations['real_number_float'])
            return {"success": True, "result": result}
        except ValueError:
            return {"success": False, "error": "Input is not a real number"}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, calculator_informations: Dict):
        """ Convert parameter that should be a number (but is a string) to a number and check type
        :param  - calculator_informations: calculator informations
        """
        calculator_informations['real_number_float'] = float(calculator_informations['real_number'])
        validate_entry = (
            isinstance(calculator_informations['real_number_float'], float)
        )
        if not validate_entry:
            raise

    def __calculate(self, real_number_int: float) -> float:
        """ Doing the calculation of the first calculator
        :param  - real_number_int: float input
        :return - Result of the first calculator
        """
        one_third = real_number_int / 3
        first_result = calculate_sqrt(one_third / 4 + 7)
        second_result = one_third ** 2.121 / 5 + 1
        third_result = one_third
        return calculate_average([first_result, second_result, third_result])
