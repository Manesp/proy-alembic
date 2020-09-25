import sqlalchemy

from . import db
from flask import request,jsonify

class User(db.Model):
    __versioned__ = {'strategy': 'subquery'}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(1000))

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'surname': self.surname
        }

def NewUser():
    name = request.json['name'],
    surname = request.json['surname'],
    insert = User(name,surname)
    db.session.add(insert)
    db.session.commit()


