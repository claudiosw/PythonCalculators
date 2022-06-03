import os


class RunSecondCalculatorView:
    """ View class of the second calculator
    """

    def __init__(self):
        self.__input_list = []

    def run_second_calculator_page(self) -> any:
        """ What is shown when the user chooses the second calculator
        :return - Dictionary with list of the input numbers
        """
        self.__clear()

        print('Second Calculator \n\n')
        while(True):
            input_number = input('Press a number and ENTER or just ENTER if you are done: ')
            if input_number:
                self.__input_list.append(input_number)
            else:
                break
        return {
            "list_real_numbers": self.__input_list
        }

    def run_second_calculator_success(self, second_calculator_registry: any) -> None:
        """ View shown if second calculator is sucessful
        :param  - second_calculator_registry: Dictionary with the result
        """
        self.__clear()

        message = f'''
            {self.__basic_message(self.__input_list)}
            Result: { second_calculator_registry["result"] }
            Success!
        '''

        print(message)

    def run_second_calculator_fail(self, error: str) -> None:
        """ View shown if second calculator fails
        :param  - error: Error that must be shown
        """
        self.__clear()

        message = f'''
            Ocurred an error to run the second calculator.
            {self.__basic_message(self.__input_list)}
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
            Second Calculator
            Input: { input }
        '''
