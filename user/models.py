__author__ = 'Joshua'

from SeraphNav import db
from website.models import Nav


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(35), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    is_admin = db.Column(db.Boolean)


    def __init__(self, email, username, password, is_admin=False):
        self.email = email
        self.username = username
        self.password = password
        self.is_admin = is_admin


    def __repr__(self):
        return '<User %r>' % self.username