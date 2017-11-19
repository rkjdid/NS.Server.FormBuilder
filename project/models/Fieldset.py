# -*- coding: utf8 -*-

from sqlalchemy import *
from sqlalchemy.orm import relationship
from .. import db


class Fieldset(db.Model):

    __tablename__ = 'Fieldset'

    pk_Fieldset = Column(BigInteger, primary_key=True)

    fk_form = Column(ForeignKey('Form.pk_Form'), nullable=False)

    legend = Column(String(255, 'BINARY'), nullable=False)
    fields = Column(String(255, 'BINARY'), nullable=False)
    multiple = Column(Boolean, nullable=True)
    curStatus = Column(Integer, nullable=False)
    refid = Column(String(255, 'BINARY'), nullable=False)
    order = Column(SmallInteger, nullable=False)

    Form = relationship('Form')

    def __init__(self, legend, fields, multiple, refid, order):
        self.legend = legend
        self.fields = fields
        self.multiple = multiple
        self.curStatus = 0
        self.refid = refid
        self.order = order

    def update(self, legend, fields, multiple, refid, order):
        self.legend = legend
        self.fields = fields
        self.multiple = multiple
        self.refid = refid
        self.order = order

    def toJSON(self):
        return {
            "legend"    : self.legend,
            "fields"    : self.fields.split(',') if len(self.fields)> 0 else [],
            "multiple"  : self.multiple,
            "refid"     : self.refid,
            "order"     : self.order
        }

    @classmethod
    def getColumnsList(cls):
        return [
            "legend",
            "fields",
            "multiple",
            "refid",
            "order"
        ]