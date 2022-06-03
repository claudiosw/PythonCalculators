from typing import List, Dict
from .dependencies.math_dependencies import calculate_standard_deviation


class RunSecondCalculatorController:
    """ Class to define second calculator """

    def run(self, calculator_informations: Dict) -> Dict[bool, float]:
        """ Run second calculator
        :param  - calculator_informations: calculator informations
        :return - Dictionary with informations of the process
        """

        try:
            self.__convert_validate(calculator_informations)
            result = self.__calculate(calculator_informations['list_real_numbers_float'])
            return {"success": True, "result": result}
        except ValueError:
            return {"success": False, "error": "At least one input is not a real number"}
        except Exception as exception:
            return {"success": False, "error": str(exception)}

    def __convert_validate(self, calculator_informations: Dict):
        """ Convert parameter that should be a number (but is a string) to a number and check type
        :param  - calculator_informations: calculator informations
        """
        calculator_informations['list_real_numbers_float'] = [
            float(item) for item in calculator_informations['list_real_numbers']
        ]
        validate_entry = (
            all(isinstance(item, float) for item in calculator_informations['list_real_numbers_float'])
        )
        if not validate_entry:
            raise

    def __calculate(self, numbers_list: List[float]) -> float:
        """ Doing the calculation of the second calculator
        :param  - numbers_list: list of float numbers
        :return - Result of the second calculator
        """
        calculated_list = [(item * 11) ** 0.95 for item in numbers_list]
        return 1 / calculate_standard_deviation(calculated_list)
