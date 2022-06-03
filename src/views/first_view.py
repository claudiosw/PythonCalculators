def introduction_page():
    """ View that is shown when the program is executed for the first time
    """
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
