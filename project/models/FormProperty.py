# -*- coding: utf8 -*-

from sqlalchemy import *
from sqlalchemy.orm import relationship
from .. import db
import datetime


# Form Property
class FormProperty(db.Model):

    __tablename__    = 'FormProperty'

    pk_FormProperty  = Column(BigInteger, primary_key=True)

    fk_Form          = Column(ForeignKey('Form.pk_Form'), nullable=False)

    name             = Column(String(255, 'BINARY'), nullable=False)
    value            = Column(String(255, 'BINARY'), nullable=False)
    creationDate     = Column(DateTime, nullable=False)
    valueType        = Column(String(10, 'BINARY'), nullable=False)

    Form = relationship('Form')

    # Constructor
    def __init__(self, name, value, valueType):
        self.name         = name
        self.value        = value
        self.valueType    = valueType
        self.creationDate = datetime.datetime.now()

    # Return value casted on the correct format
    def getvalue(self):
        try:
            if self.valueType == "Boolean":
                print ('form ' + self.value in ['true', 'yes', '1', 'True'])
                return self.value in ['true', 'yes', '1', 'True']
            elif self.valueType == "Number":
                return int(self.value)
            elif self.valueType == "Double":
                return float(int(self.value))
            else:
                return self.value
        except:
            return self.value

    def update(self, newName, newValue, newCreationDate, newValueType):
        self.name           = newName
        self.value          = newValue
        self.creationDate   = newCreationDate
        self.valueType      = newValueType