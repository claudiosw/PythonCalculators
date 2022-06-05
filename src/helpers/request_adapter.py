from typing import Type
from flask import request as FlaskRequest
from src.models.http_types.http_response import HttpResponse
from src.controllers.interfaces.calculators_interface import CalculatorsInterface


def request_adapter(request: FlaskRequest, process: Type[CalculatorsInterface]):
    '''
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_param=request.args,
        url=request.full_path,
    )'''
    # http_response = process.run(http_request)
    data = request.get_json()
    calculator_informations = {"real_number": data["real_number"]}

    result = process.run(calculator_informations)
    http_response = HttpResponse()
    if result['success']:
        http_response.body = result['result']
        http_response.status_code = 200
    else:
        http_response.body = result['error']
        http_response.status_code = 400

    return http_response
