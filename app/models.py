from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/Users'

db = SQLAlchemy(app)

class Users(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   age = db.Column(db.String(100))
   phoneNumber = db.Column(db.String(100))

   '''def __init__(self,id ,name,age,phoneNumber):
       self.id = id
       self.name = name
       self.age = age
       self.phoneNumber = phoneNumber'''

db.create_all()
