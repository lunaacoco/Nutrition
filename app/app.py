from flask import Flask
from . import recipelist, simple_pages
from app.extentions.database import db, migrate

#This file brings all templates and the database together and initialises the Flask server to be run 

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_extentions(app)
    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(recipelist.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)
    app.register_blueprint(addrecipe.routes.blueprint)

def register_extentions(app: Flask):
    db.init_app(app)
    migrate.init_app(app, db)


