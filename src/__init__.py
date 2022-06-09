from flask import Flask


def create_app():
    """ Construct the core application """
    app = Flask(__name__)

    with app.app_context():
        from .routers.calculators_routers import calculators_bp
        app.register_blueprint(calculators_bp)
        return app
