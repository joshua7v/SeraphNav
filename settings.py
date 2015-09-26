__author__ = 'Joshua'

SECRET_KEY = 'your secret key'
DEBUG = True
DB_USERNAME = 'your db username'
DB_PASSWORD = 'your db pwd'
SERAPHNAV_DATABASE_NAME = 'your db name'
SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@host-name:3306/%s?charset=utf8' % (DB_USERNAME, DB_PASSWORD, SERAPHNAV_DATABASE_NAME)
SALT = 'your password salt'