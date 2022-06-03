from flask import Blueprint, request
from flask import jsonify
from src.controllers.run_first_calculator_controller import RunFirstCalculatorController

# Blueprint Configuration
calculators_bp = Blueprint(
    'calculators_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@calculators_bp.route('/calculators/<calculator_number>', methods=['POST'])
def calculators(calculator_number):
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            if calculator_number == '1':
                run_first_calculator_controller = RunFirstCalculatorController()
                calculator_informations = {"real_number": data["real_number"]}
                result = run_first_calculator_controller.run(calculator_informations)
                return jsonify(result)
            return jsonify("Invalid Calculator number")
        return jsonify("Request type is not json")
