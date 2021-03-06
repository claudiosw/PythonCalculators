from src.controllers.run_first_calculator_controller import RunFirstCalculatorController
from src.controllers.run_second_calculator_controller import RunSecondCalculatorController
from src.controllers.run_third_calculator_controller import RunThirdCalculatorController
from src.helpers.request_adapter import request_adapter
from flask import Blueprint, request, jsonify


# Blueprint Configuration
calculators_bp = Blueprint(
    'calculators_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@calculators_bp.route('/calculator_1', methods=['POST'])
def calculator_1():
    """ Router of the Calculator 1
        :return - Response and status code
    """
    http_response = request_adapter(request, RunFirstCalculatorController())
    return jsonify(http_response.body), http_response.status_code


@calculators_bp.route('/calculator_2', methods=['POST'])
def calculator_2():
    """ Router of the Calculator 2
        :return - Response and status code
    """
    http_response = request_adapter(request, RunSecondCalculatorController())
    return jsonify(http_response.body), http_response.status_code


@calculators_bp.route('/calculator_3', methods=['POST'])
def calculator_3():
    """ Router of the Calculator 3
        :return - Response and status code
    """
    http_response = request_adapter(request, RunThirdCalculatorController())
    return jsonify(http_response.body), http_response.status_code
