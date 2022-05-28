import os


class RunFirstCalculatorView:

    def __init__(self):
        self.__input = None

    def run_first_calculator_page(self) -> str:
        self.__clear()

        print('First Calculator \n\n')
        self.__input = input('Real Number: ')
        return  {
            "real_number": self.__input
        }
    
    def run_first_calculator_success(self, first_calculator_registry: any) -> None:
        self.__clear()

        message = f'''
            {self.__basic_message(self.__input)}
            Result: { first_calculator_registry["result"] }
            Success!
        '''

        print(message)
    
    def run_first_calculator_fail(self, error: str) -> None:
        # self.__clear()

        message = f'''
            Ocurred an error to run the first calculator.
            {self.__basic_message(self.__input)}
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')

    
    def __basic_message(self, input: float) -> str:
        return f'''
            First Calculator
            Input: { input }
        '''
