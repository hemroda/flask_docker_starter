from flask.cli import FlaskGroup

from main import app, db
from blueprints.admin.models.user import User


cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_first_user")
def seed_first_user():
    db.session.add(User(email="jsmith@flask_docker_starter.com"))
    db.session.commit()


if __name__ == "__main__":
    cli()
