from flask import Blueprint, render_template, request, flash, redirect
from .models import Recipe
from sqlalchemy import and_



blueprint = Blueprint('recipelist', __name__)

@blueprint.post('/recipelist')
def post_recipelist():
    minkcal = 0
    maxkcal = 10000
    mincarbs = 0
    maxcarbs = 1000
    minprotein = 0
    maxprotein = 1000
    minfat = 0
    maxfat = 1000
    #the variables above give a base value to the filter, so that if nothing is given in the form,
    #the filter will "ignore" it by just giving everything between this ridiculous high values

    #below is then the if statements to update the minimum and maximum of the filters
    if request.form['kcal'] != '':
        kcal = int(request.form['kcal'])
        minkcal = kcal - 200
        maxkcal = kcal + 200
    if request.form['carbs'] != '':
        carbs = int(request.form['carbs'])
        mincarbs = carbs - 10
        maxcarbs = carbs + 10
    if request.form['protein'] != '':
        protein = int(request.form['protein'])
        minprotein = protein - 10
        maxprotein = protein + 10
    if request.form['fat'] != '':
        fat = int(request.form['fat'])
        minfat = fat - 10
        maxfat = fat + 10


    #here the database will then be filtered with the values
    #I have tried probably a thousand different ideas and landed onto this one,
    # im sure it won't be the best solution but i am happy that it works

    recipes = Recipe.query.filter(
        and_(
            Recipe.kcal >= minkcal, Recipe.kcal <= maxkcal
        ),
        and_(
            Recipe.carbs >= mincarbs, Recipe.carbs <= maxcarbs
        ),
        and_(
            Recipe.protein >= minprotein, Recipe.protein <= maxprotein
        ),
        and_(
            Recipe.fat >= minfat, Recipe.fat <= maxfat
        )
    )

    return render_template('recipelist/index2.html', recipes=recipes)

@blueprint.get('/recipelist')
def get_recipelist():
    all_recipes = Recipe.query.all()
    return render_template('recipelist/index2.html', recipes=all_recipes)


@blueprint.route('/recipe/<id>')
def recipe(id):
    recipe = Recipe.query.get(id)
    print(recipe)
    return render_template('recipe/index2.html', recipe=recipe)



#The first data to feed into routes
"""
recipe_data = {
    'omelette' : {'name': 'Omelette', 'kcal': 233, 'carbs': 25, 'protein': 44, 'fat': 23},
    'pork' : {'name': 'Pork', 'kcal': 237, 'carbs': 224, 'protein': 457, 'fat': 224},
    'chicken' : {'name': 'Chicken', 'kcal': 2543, 'carbs': 236, 'protein': 879, 'fat': 243},
    'omelette' : {'name': 'Omelette', 'kcal': 233, 'carbs': 25, 'protein': 44, 'fat': 23}
}
"""

#test to see how reading a file works

"""@blueprint.route('/Omelettetest')
def Omelettetest():
    with open('c:/Users/emily/Programmierenzeugs/Nutrition/app/recipelist/rezept.txt') as f:
        name = f.readline()
        kcal = f.readline()
        carbs = f.readline()
        content = f.read()
    return render_template('recipelist/index2.html', name=name, kcal=kcal, carbs=carbs, content=content)
"""

#first blueprints without the database

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

