def introduction_page():
    message = '''
        Calculators System

        * Run First Calculator - 1
        * Run Second Calculator - 2
        * Run Third Calculator - 3
        * Exit - 4
    '''

    print(message)
    command = input('Command: ')

    return command
