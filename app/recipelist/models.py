from app.extentions.database import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80))
    kcal = db.Column(db.Integer)
    carbs = db.Column(db.Numeric(5, 2)) #5 is whole length, 2 is the decimal numbers contained in the first number 5
    protein = db.Column(db.Numeric(5, 2))
    fat = db.Column(db.Numeric(5, 2))