from app.extentions.database import db
from datetime import datetime

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug=db.Column(db.String(80), unique = True) #String ist max 80 Zeichen lang
    name = db.Column(db.String(80))
    kcal = db.Column(db.Integer)
    carbs = db.Column(db.Numeric(5, 2)) #5 is whole length, 2 is the decimal numbers contained in the first number 5
    protein = db.Column(db.Numeric(5, 2))
    fat = db.Column(db.Numeric(5, 2))
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    picture_url = db.Column(db.String(256))
    ingredients = db.Column(db.String)
    content = db.Column(db.String)


    