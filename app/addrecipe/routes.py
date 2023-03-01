from flask import Blueprint, render_template, request
from app.recipelist.models import Recipe
from app.extentions.database import db


blueprint = Blueprint('addrecipe', __name__)

#render Template for adding the recipe

@blueprint.get('/addrecipe')
def get_addrecipe():
    return render_template('addrecipe/index.html')

@blueprint.post('/addrecipe')
def post_addrecipe():
    name = request.form['name']
    slug = request.form['slug']
    kcal = int(request.form['kcal'])
    carbs = (request.form['carbs'])
    protein = request.form['protein']
    fat = request.form['fat']
    picture_url = '../../static/images/' + slug + '.jpg'
    ingredients = request.form['ingredients']
    content = request.form['Instructions']

    new_recipe = Recipe(name=name,slug=slug,  kcal=kcal, carbs=carbs, protein=protein, fat=fat,picture_url=picture_url, ingredients=ingredients, content=content)
    db.session.add(new_recipe)
    db.session.commit()
    return render_template('addrecipe/success.html')