from flask import Blueprint, current_app, render_template

bp = Blueprint("main", __name__)


@bp.route("/")
def index():
    return render_template("index.html", service_email=current_app.config["SERVICE_EMAIL"])

@bp.route("/privacy")
def privacy():
    return render_template("privacy.html")