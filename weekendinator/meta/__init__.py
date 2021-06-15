from flask import Blueprint, render_template

bp = Blueprint("meta", __name__)

@bp.route("/")
def home():
    return render_template("home.html")
