from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    userName = db.Column(db.String(150), unique=False)
    password = db.Column(db.String(150))

    reviews = db.relationship('Review')


class tempUser(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    temp_mail = db.Column(db.String(150), unique=False)
    temp_userName = db.Column(db.String(150), unique=False)
    temp_password = db.Column(db.String(150))

    def __init__(self, temp_mail, temp_userName, temp_password):
        self.temp_mail = temp_mail
        self.temp_userName = temp_userName
        self.temp_password = temp_password



class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Text)
    rating=db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class 