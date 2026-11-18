import os

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config["DATABASE"] = os.path.join(app.instance_path, "emailchecker.sqlite")
    app.config["SERVICE_EMAIL"] = "check@example.com"  # placeholder until the inbox is set up (step 5)
    os.makedirs(app.instance_path, exist_ok=True)

    from . import db
    db.init_app(app)

    from . import main
    app.register_blueprint(main.bp)

    return app