__author__ = 'Joshua'

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeraphNav import app
import sqlalchemy


db_uri = 'mysql://%s:%s@192.168.99.100:3306/' % (app.config['DB_USERNAME'], app.config['DB_PASSWORD'])
engine = sqlalchemy.create_engine(db_uri, encoding='utf8', convert_unicode=True)
conn = engine.connect()
conn.execute("commit")
conn.execute("CREATE DATABASE " + app.config['SERAPHNAV_DATABASE_NAME'])
conn.close()
