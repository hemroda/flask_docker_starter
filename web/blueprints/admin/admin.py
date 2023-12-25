from flask import Flask, Blueprint, render_template, redirect

from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

admin_bp = Blueprint(
    "admin", __name__, template_folder="templates", static_folder="static"
)


@admin_bp.route("/admin")
def homepage():
    return render_template("admin/homepage.html", username="John Smith")
