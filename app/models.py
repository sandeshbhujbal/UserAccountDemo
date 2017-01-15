from app import db
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(128))
  email = db.Column(db.String(128))
  age = db.Column(db.Integer)
  gender = db.Column(db.String(128))
  phoneNumber = db.Column(db.String(128))
