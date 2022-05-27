from .constructor.introduction_process import introduction_process
from .constructor.run_first_calculator_process import run_first_calculator_process

def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': run_first_calculator_process()
        elif command == '4': exit()
        else: print('\nCommand not found, try again!\n\n')
