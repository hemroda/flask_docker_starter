from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap5

from blueprints.pages.pages import pages_bp
from blueprints.flashcards.flashcards import flashcards_bp
from blueprints.weshop.weshop import weshop_bp

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

bootstrap = Bootstrap5(app)

app.register_blueprint(pages_bp)
app.register_blueprint(flashcards_bp)
app.register_blueprint(weshop_bp)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True, nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)

    def __init__(self, email):
        self.email = email


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
