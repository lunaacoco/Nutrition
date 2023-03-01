from app.extentions.database import db

class CRUDMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return self

class User(db.Model, CRUDMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), index=True, unique = True)
    password = db.Column(1024)
