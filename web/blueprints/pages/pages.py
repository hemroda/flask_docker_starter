from flask import (Flask, Blueprint, render_template, redirect)

from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

pages_bp = Blueprint('pages', __name__, template_folder='templates', static_folder='static')


@pages_bp.route("/")
def homepage():
    return render_template("pages/homepage.html", username="John Smith")


@pages_bp.route("/about")
def about():
    return render_template("pages/about.html")
