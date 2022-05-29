import os


class RunThirdCalculatorView:

    def __init__(self):
        self.__input_list = []

    def run_third_calculator_page(self) -> str:
        # self.__clear()

        print('Third Calculator \n\n')
        while(True):
            input_number = input('Press a number and ENTER or just ENTER if you are done: ')
            if input_number:
                self.__input_list.append(input_number)
            else:
                break
        return  {
            "list_real_numbers": self.__input_list
        }
    
    def run_third_calculator_success(self, third_calculator_registry: any) -> None:
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
        # self.__clear()

        message = f'''
            Ocurred an error to run the third calculator.
            {self.__basic_message(self.__input_list)}
        '''
        print(message)

    def __clear(self):
        os.system('cls||clear')

    
    def __basic_message(self, input: float) -> str:
        return f'''
            Third Calculator
            Input: { input }
        '''
