# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask('formbuilder')
app.debug = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///formbuilder.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])

engine = db

# session = scoped_session(sessionmaker(bind=db))
session = db.create_scoped_session()

# Base = db.make_declarative_base(declarative_base())
# Base = declarative_base()
# Base.metadata.create_all(db)


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()

from project.controllers import *
