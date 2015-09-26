__author__ = 'Joshua'

from SeraphNav import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password


    def __repr__(self):
        return '<User %r>' % self.username