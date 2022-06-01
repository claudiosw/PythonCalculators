import os


class RunFirstCalculatorView:
    """ View class of the first calculator
    """

    def __init__(self):
        self.__input = None

    def run_first_calculator_page(self) -> any:
        """ What is shown when the user chooses the first calculator Dict[str]
        :return - Dictionary with list of the input numbers
        """
        self.__clear()

        print('First Calculator \n\n')
        self.__input = input('Real Number: ')
        return {
            "real_number": self.__input
        }

    def run_first_calculator_success(self, first_calculator_registry: any) -> None:
        """ View shown if first calculator is sucessful
        :param  - first_calculator_registry: Dictionary with the result
        """
        self.__clear()

        message = f'''
            {self.__basic_message(self.__input)}
            Result: { first_calculator_registry["result"] }
            Success!
        '''

        print(message)

    def run_first_calculator_fail(self, error: str) -> None:
        """ View shown if first calculator fails
        :param  - error: Error that must be shown
        """
        self.__clear()

        message = f'''
            Ocurred an error to run the first calculator.
            {self.__basic_message(self.__input)}
            Error: {error}
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')

    def __basic_message(self, input: float) -> str:
        """ Basic message that must be shown
        :param  - input: Input provided by the user
        """
        return f'''
            First Calculator
            Input: { input }
        '''
