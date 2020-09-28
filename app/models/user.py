import sqlalchemy

from . import db
from flask import request,jsonify

class User(db.Model):
    __versioned__ = {'strategy': 'subquery'}
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(1000))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }


