__author__ = 'Joshua'

from app import db


class Site(db.Document):
    title = db.StringField()
    desc = db.StringField()
    url = db.StringField()

    def __str__(self):
        return "title: {} - desc: {} - desc: {}".format(self.title, self.desc, self.url)