import os


class RunSecondCalculatorView:

    def __init__(self):
        self.__input_list = []

    def run_second_calculator_page(self) -> str:
        # self.__clear()

        print('Second Calculator \n\n')
        while(True):
            input_number = input('Press a number and ENTER or just ENTER if you are done: ')
            if input_number:
                self.__input_list.append(input_number)
            else:
                break
        return  {
            "list_real_numbers": self.__input_list
        }
    
    def run_second_calculator_success(self, second_calculator_registry: any) -> None:
        self.__clear()

        message = f'''
            {self.__basic_message(self.__input_list)}
            Result: { second_calculator_registry["result"] }
            Success!
        '''

        print(message)
    
    def run_second_calculator_fail(self, error: str) -> None:
        # self.__clear()

        message = f'''
            Ocurred an error to run the second calculator.
            {self.__basic_message(self.__input_list)}
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')

    
    def __basic_message(self, input: float) -> str:
        return f'''
            Second Calculator
            Input: { input }
        '''
