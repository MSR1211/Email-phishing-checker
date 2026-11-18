import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["DATABASE"] = os.path.join(app.instance_path, "emailchecker.sqlite")
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    @app.route("/")
    def index():
        return "EmailChecker is running"

    return app

