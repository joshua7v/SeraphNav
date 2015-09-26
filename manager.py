__author__ = 'Joshua'

import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server
from flask.ext.migrate import MigrateCommand
from SeraphNav import app

manager = Manager(app)

manager.add_command('db', MigrateCommand)

manager.add_command('runserver', Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0',
    port = '9000'
))


if __name__ == '__main__':
    manager.run()