from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from flask_bootstrap import Bootstrap5

from blueprints.pages.pages import pages_bp
from blueprints.admin.admin import admin_bp

app = Flask(__name__)
app.config.from_object("config.Config")

db = SQLAlchemy(app)

bootstrap = Bootstrap5(app)

app.register_blueprint(pages_bp)
app.register_blueprint(admin_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
