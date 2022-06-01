from src.views.first_view import introduction_page


def introduction_process():
    """ Process that is run when it is executed for the first time
    """
    command = introduction_page()
    return command
