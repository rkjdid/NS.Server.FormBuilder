# -*- coding: utf8 -*-

import datetime
from sqlalchemy import *
from sqlalchemy.orm import relationship
from .. import db


# Relation between Form and KeyWord
class KeyWord_Form(db.Model):

    __tablename__ = "KeyWord_Form"

    pk_KeyWord_Form = Column(BigInteger, primary_key=True)

    fk_KeyWord      = Column(ForeignKey('KeyWord.pk_KeyWord'), nullable=False)
    fk_Form         = Column(ForeignKey('Form.pk_Form'), nullable=False)

    creationDate    = Column(DateTime, nullable=False)
    curStatus       = Column(Integer, nullable=False)

    Form    = relationship('Form')
    KeyWord = relationship('KeyWord')

    #   Constructor
    def __init__(self):
        self.creationDate = datetime.datetime.now()
        self.ModifDate = datetime.datetime.now()
        self.curStatus = "1"

    # JSON serialization
    def toJSON(self):
        return self.KeyWord.toJSON()

    def setForm(self, formToSet):
        self.Form = formToSet
        self.fk_Form = self.Form.pk_Form

    def setKeyWord(self, keywordToSet):
        self.KeyWord = keywordToSet
        self.fk_KeyWord = self.KeyWord.pk_KeyWord