'''
SQLAlchemy models for AppName
'''


from flask.ext.sqlalchemy import SQLAlchemy
from enum import Enum

from app.sms import carriers


db = SQLAlchemy()

carrier_slugs = carriers.keys()


class User(db.Model):
    '''Represent a user that can sign up for AppName'''
    carrier = db.Column(db.Enum(*carrier_slugs, name='Carriers'))
    phone_number = db.Column(db.BigInteger, primary_key=True)
    confirm_code = db.Column(db.Integer)
    confirmed = db.Column(db.Boolean)

    def __init__(self, carrier, phone_number, confirm_code):
        self.carrier = carrier
        self.phone_number = phone_number
        self.confirm_code = confirm_code
        self.confirmed = False
