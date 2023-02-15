from flask import Flask, render_template
from . import recipelist, simple_pages
from app.extentions.database import db, migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extentions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(recipelist.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)

def register_extentions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


