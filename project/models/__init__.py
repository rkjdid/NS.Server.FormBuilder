# -*- coding: utf8 -*-Follow


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import json

from .base import Base
from . import Form
from . import Input
from . import InputProperty
from . import Unity
from . import KeyWord
from . import KeyWord_Form
from . import ConfiguratedInput
from . import ConfiguratedInputProperty
from . import Fieldset


# Database connexion
# We use pyodbc and SQL Server for the moment
with open("project/config/config.json", "r") as config:
        data = json.loads( config.read() )
sqlConnexion = data["sql"]["url"] if 'sql' in data and 'url' in data['sql'] else 'mssql+pyodbc://CORLEONE-PC/formbuilder'

engine = create_engine(sqlConnexion)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
