from typing import Type
from flask import request as FlaskRequest
from src.models.http_types.http_response import HttpResponse
from src.models.http_types.http_request import HttpRequest
from src.controllers.interfaces.calculators_interface import CalculatorsInterface


def request_adapter(request: FlaskRequest, process: Type[CalculatorsInterface]) -> Type[HttpResponse]:
    http_request = HttpRequest(
        header=request.headers,
        body=request.json,
        query_param=request.args,
        url=request.full_path,
    )

    result = process.run(http_request)
    http_response = HttpResponse()
    if result['success']:
        http_response.body = result['result']
        http_response.status_code = 200
    else:
        http_response.body = f"Error: {result['error']}"
        http_response.status_code = 400

    return http_response
