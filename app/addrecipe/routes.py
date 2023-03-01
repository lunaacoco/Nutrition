from flask import Blueprint, render_template

blueprint = Blueprint('addrecipe', __name__)

#render Template for adding the recipe

@blueprint.get('/addrecipe')
def get_addrecipe():
    return render_template('addrecipe/index.html')