from flask import Blueprint, render_template

blueprint = Blueprint('simple_pages', __name__)


#render blueprint for index page
@blueprint.route('/')
def index():
    return render_template('simple_pages/index.html')

@blueprint.route('/test')
def test():
    return render_template('simple_pages/test.html')