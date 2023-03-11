from flask import Flask


def create_app(config_type=None):
    app = Flask(__name__, instance_relative_config=True)

    if config_type is None:
        try:
            app.config.from_pyfile("config.py")
        except FileNotFoundError:
            pass
    else:
        app.config.update(config_type)

    from .main.routes import main
    app.register_blueprint(main)

    return app
