from flask import Flask

from flask_bootstrap import Bootstrap5

from blueprints.pages.pages import pages_bp

app = Flask(__name__)

bootstrap = Bootstrap5(app)

app.register_blueprint(pages_bp)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
