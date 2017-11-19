#!/usr/bin/env python
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from project import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def runserver():
    app.run('0.0.0.0')

if __name__ == '__main__':
    manager.run()
