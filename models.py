from flask_login import UserMixin
from . import db
from sqlalchemy.sql import func 

class User(db.Model, UserMixin):
     id = db.Column(db.Integer, primary_key = True)
     email = db.Column(db.String(150), unique = True)
     password = db.Column(db.String(150))
     first_name = db.Column(db.String(150))
     notes = db.relationship('Note')
     graph = db.relationship('graph')

class Note(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone = True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class graph(db.Model):
     id = db.Column(db.Integer, primary_key = True)
     expense_type = db.Column(db.String(10000), nullable = False)
     expense_amount = db.Column(db.Float) 
     date = db.Column(db.DateTime(timezone = True), default = func.now())
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
