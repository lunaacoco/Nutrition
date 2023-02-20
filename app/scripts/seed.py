from app.app import create_app
from app.recipelist.models import Recipe
from app.extentions.database import db


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()

"""
new_recipe = Recipe(
    slug= 'pancake-waffle',
    name = 'pancake waffle',
    kcal = 200,
    carbs = 400,
    protein = 12,
    fat = 30,
    picture_url = 'https://source.unsplash.com/random/?waffle',
    ingredients = 'pancake, flour, egg, sugar',
    content = 'gather all ingredients, mix them together, bake it, eat it'
)
db.session.add(new_recipe)
"""

"""
recipe_data = {
    'omelette' : {'name': 'Omelette', 'kcal': 233, 'carbs': 25, 'protein': 44, 'fat': 23, 'ingredients' : 'milk butter oil', 'content' : 'put together add milk heat up in pan'},
    'pork' : {'name': 'Pork', 'kcal': 237, 'carbs': 224, 'protein': 457, 'fat': 224, 'ingredients' : 'milk butter oil', 'content' : 'put together add milk heat up in pan'},
    'chicken' : {'name': 'Chicken', 'kcal': 2543, 'carbs': 236, 'protein': 879, 'fat': 243, 'ingredients' : 'milk butter oil', 'content' : 'put together add milk heat up in pan'},
    'pita' : {'name': 'Pitabread', 'kcal': 237, 'carbs': 25, 'protein': 47, 'fat': 23, 'ingredients' : 'milk butter oil', 'content' : 'put together add milk heat up in pan'}
}


for slug, recipe in recipe_data.items():
  new_recipe = Recipe(slug=slug, name=recipe['name'], kcal=recipe['kcal'], carbs=recipe['carbs'], protein=recipe['protein'], fat=recipe['fat'], picture_url = '../app/static/images/' + slug + '.jpg', ingredients=recipe['ingredients'], content=recipe['content'])
  db.session.add(new_recipe)
"""
with open('C:/users/emily/programmierenzeugs/nutrition/app/scripts/recipe.txt') as recipe:
    name = recipe.readline()
    slug = recipe.readline()
    kcal = int(recipe.readline())
    carbs = recipe.readline()
    protein = recipe.readline()
    fat = recipe.readline()
    picture_url = '../../static/images/' + slug + '.jpg'
    ingredients = recipe.readline()
    content = recipe.read()

new_recipe = Recipe(name=name, slug=slug, kcal=kcal, carbs=carbs, protein=protein, fat=fat, picture_url=picture_url, ingredients=ingredients, content=content)
db.session.add(new_recipe)



db.session.commit()