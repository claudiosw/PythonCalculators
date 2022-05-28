from typing import List, Dict
from .dependencies.math_dependencies import calculate_sqrt, calculate_average, calculate_standard_deviation

class RunSecondCalculatorController:
    """ Class to define second calculator """

    def run(self, calculator_informations: Dict) -> Dict[bool, float]:
        """Run second calculator
        :param  - calculator_informations: calculator informations
        :return - Dictionary with informations of the process
        """

        response = None

        try:
            print("start")
            self.__convert_validate(calculator_informations)
            print(f"calculator_informations={calculator_informations}")
            result = self.__calculate(calculator_informations['list_real_numbers_float'])
            print(f"result={result}")
            return { "success": True, "result": result }
        except Exception as exception:
            return { "success": False, "error": str(exception) }

    def __convert_validate(self, calculator_informations: Dict):
        try:
            calculator_informations['list_real_numbers_float'] = [float(item) for item in calculator_informations['list_real_numbers']]
            validate_entry = (
                all(isinstance(item, float) for item in calculator_informations['list_real_numbers_float'])
            )
            if not validate_entry:
                raise
        except ValueError:
            raise ValueError("At least one input is not a real number")

    def __calculate(self, numbers_list: List[float]) -> float:
        calculated_list = [ (item * 11) ** 0.95 for item in numbers_list]
        return 1 / calculate_standard_deviation(calculated_list)
