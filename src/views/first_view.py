def introduction_page():
    message = '''
        Calculators System

        * Run First Calculator - 1
        * Run Second Calculator - 2
        * Exit - 4
    '''

    print(message)
    command = input('Command: ')

    return command
