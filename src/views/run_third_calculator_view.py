import os
from typing import List


class RunThirdCalculatorView:
    """ View class of the third calculator
    """

    def __init__(self):
        self.__input_list = []

    def run_third_calculator_page(self) -> any:
        """ Process that is run when the uses chooses the third calculator
            Calls the respectives controllers and views
        :return - Dictionary with list of the input numbers
        """
        self.__clear()

        print('Third Calculator \n\n')
        while(True):
            input_number = input('Press a number and ENTER or just ENTER if you are done: ')
            if input_number:
                self.__input_list.append(input_number)
            else:
                break
        return {
            "list_real_numbers": self.__input_list
        }

    def run_third_calculator_success(self, third_calculator_registry: any) -> None:
        """ View shown if third calculator is sucessful
        :param  - third_calculator_registry: Dictionary with the result
        """
        self.__clear()
        if third_calculator_registry['result']:
            status = 'Success!'
        else:
            status = 'Failed!!!'
        message = f'''
            {self.__basic_message(self.__input_list)}
            Result: { third_calculator_registry["result"] }
            {status}
        '''

        print(message)

    def run_third_calculator_fail(self, error: str) -> None:
        """ View shown if third calculator fails
        :param  - error: Error that must be shown
        """
        self.__clear()

        message = f'''
            Ocurred an error to run the third calculator.
            {self.__basic_message(self.__input_list)}
            Error: {error}
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')

    def __basic_message(self, input_list: List[float]) -> str:
        """ Basic message that must be shown
        :param  - input: Input provided by the user
        """
        return f'''
            Third Calculator
            Input: { input_list }
        '''
