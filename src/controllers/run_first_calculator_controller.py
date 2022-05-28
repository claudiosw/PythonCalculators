from typing import Dict
from .dependencies.math_dependencies import calculate_sqrt, calculate_average

class RunFirstCalculatorController:
    """ Class to define first calculator """

    def run(self, calculator_informations: Dict) -> Dict[bool, float]:
        """Run first calculator
        :param  - calculator_informations: calculator informations
        :return - Dictionary with informations of the process
        """

        response = None

        try:
            print("start")
            self.__convert_validate(calculator_informations)
            print(f"calculator_informations={calculator_informations}")
            result = self.__calculate(calculator_informations['real_number_int'])
            print(f"result={result}")
            return { "success": True, "result": result }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __convert_validate(self, calculator_informations: Dict):
        try:
            calculator_informations['real_number_int'] = float(calculator_informations['real_number'])
            validate_entry = (
                isinstance(calculator_informations['real_number_int'], float)
            )
            if not validate_entry:
                raise
        except ValueError:
            raise ValueError("Input is not a real number")

    def __calculate(self, real_number_int: float) -> float:
        one_third = real_number_int / 3
        first_result = calculate_sqrt(one_third / 4 + 7)
        second_result = one_third ** 2.121 / 5 + 1
        third_result = one_third
        return calculate_average([first_result, second_result, third_result])
