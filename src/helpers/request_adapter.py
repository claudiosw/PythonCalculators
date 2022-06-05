from typing import Type
from flask import request as FlaskRequest
# from src.views.http_types.http_request import HttpRequest
from src.controllers.interfaces.calculators_interface import CalculatorsInterface


def request_adapter(request: FlaskRequest, process: Type[CalculatorsInterface]):
    '''
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_param=request.args,
        url=request.full_path,
    )
    http_response = process.run(http_request)'''
    data = request.get_json()
    calculator_informations = {"real_number": data["real_number"]}

    http_response = process.run(calculator_informations)
    return http_response
