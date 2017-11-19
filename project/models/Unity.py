# -*- coding: utf8 -*-

from sqlalchemy import *
from .. import db


# Unity Class
class Unity(db.Model):

    __tablename__ = "Unity"

    pk_Unity      = Column(BigInteger, primary_key=True)
    name          = Column(String(100, 'BINARY'), nullable=False)
    labelFr       = Column(String(300, 'BINARY'))
    labelEn       = Column(String(300, 'BINARY'))
    context       = Column(String(50, 'BINARY'), nullable=False)
    ordre         = Column(Integer, nullable=False)
    

    def toJSON(self):
        return {
            "ID"        : self.pk_Unity,
            "name"      : self.name,
            "labelFr"   : self.labelFr,
            "labelEn"   : self.labelEn,
            "context"   : self.context,
            "ordre"     : self.ordre
        }