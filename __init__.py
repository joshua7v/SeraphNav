__author__ = 'Joshua'

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.migrate import Migrate
import bcrypt

app = Flask(__name__)
app.config.from_object('settings')

# mongo db
# app.config['MONGODB_SETTINGS'] = {"db": "SeraphNav"}
# db = MongoEngine(app)

# db
db = SQLAlchemy(app)

# migrations
migrate = Migrate(app, db)

# salt
salt = app.config['SALT']

from website import views
from user import views


