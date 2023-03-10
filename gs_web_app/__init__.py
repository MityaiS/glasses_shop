from flask import Flask


def create_app(config_type=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_type:
        app.config.update(config_type)
    else:
        app.config.from_pyfile("config.py")

    from .main.routes import main
    app.register_blueprint(main)

    return app
