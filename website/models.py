__author__ = 'Joshua'

from SeraphNav import db
from datetime import datetime


class Nav(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin = db.Column(db.Integer, db.ForeignKey('user.id'))

    owner = db.relationship('User', backref=db.backref('nav', lazy='dynamic'), uselist=False)


    def __init__(self, admin):
        self.admin = admin


    def __repr__(self):
        return '<id %r - Admin %r>' % (self.id, self.admin)


class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nav_id = db.Column(db.Integer, db.ForeignKey('nav.id'))
    title = db.Column(db.String(80))
    desc = db.Column(db.Text)
    url = db.Column(db.String(255))
    date_added = db.Column(db.DateTime)
    seq_order = db.Column(db.Integer)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref=db.backref('sites', lazy='dynamic'))

    def __init__(self, nav, title, desc, url, category, seq_order=0, date_added=None):
        self.nav_id = nav.id
        self.title = title
        self.desc = desc
        self.url = url
        self.category = category
        if date_added is None:
            self.date_added = datetime.utcnow()
        self.seq_order = seq_order


    def __repr__(self):
        return '<Site %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    seq_order = db.Column(db.Integer)


    def __init__(self, name, seq_order=0):
        self.name = name
        self.seq_order = seq_order


    def __repr__(self):
        return '<Category %r>' % self.name