from flask import Flask, render_template
from . import recipelist, simple_pages


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config')

    register_blueprints(app)

    return app


def register_blueprints(app: Flask):
    app.register_blueprint(recipelist.routes.blueprint)
    app.register_blueprint(simple_pages.routes.blueprint)



