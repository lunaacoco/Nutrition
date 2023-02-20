from flask import Blueprint, render_template
from .models import Recipe



blueprint = Blueprint('recipelist', __name__)

"""
recipe_data = {
    'omelette' : {'name': 'Omelette', 'kcal': 233, 'carbs': 25, 'protein': 44, 'fat': 23},
    'pork' : {'name': 'Pork', 'kcal': 237, 'carbs': 224, 'protein': 457, 'fat': 224},
    'chicken' : {'name': 'Chicken', 'kcal': 2543, 'carbs': 236, 'protein': 879, 'fat': 243},
    'omelette' : {'name': 'Omelette', 'kcal': 233, 'carbs': 25, 'protein': 44, 'fat': 23}
}
"""

"""@blueprint.route('/Omelettetest')
def Omelettetest():
    with open('c:/Users/emily/Programmierenzeugs/Nutrition/app/recipelist/rezept.txt') as f:
        name = f.readline()
        kcal = f.readline()
        carbs = f.readline()
        content = f.read()
    return render_template('recipelist/index2.html', name=name, kcal=kcal, carbs=carbs, content=content)
"""


@blueprint.route('/recipelist')
def neuertest():
    all_recipes = Recipe.query.all()
    return render_template('recipelist/index2.html', recipes=all_recipes)


@blueprint.route('/recipe/<id>')
def recipe(id):
    recipe = Recipe.query.get(id)
    print(recipe)
    return render_template('recipe/index2.html', recipe=recipe)


"""@blueprint.route('/recipelist')
def recipelist():
    return render_template('recipelist/index.html', recipes=recipe_data)

@blueprint.route('/<slug>')
def recipe(slug):
    if slug in recipe_data:
        return render_template('recipe/index.html', recipename=slug, recipe=recipe_data[slug])
    else:
        return 'Sorry we could not find that recipe.'

"""

#Hier kommt dann auch die Route zuum spezifischen Rezept hin