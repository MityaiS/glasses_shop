from flask import Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    from .main.routes import main
    app.register_blueprint(main)

    return app
