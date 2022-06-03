from .constructor.introduction_process import introduction_process
from .constructor.run_first_calculator_process import run_first_calculator_process
from .constructor.run_second_calculator_process import run_second_calculator_process
from .constructor.run_third_calculator_process import run_third_calculator_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1':
            run_first_calculator_process()
        elif command == '2':
            run_second_calculator_process()
        elif command == '3':
            run_third_calculator_process()
        elif command == '4':
            exit()
        else:
            print('\nCommand not found, try again!\n\n')
