import os
from email.policy import default
from enum import unique
import requests
from click import DateTime
from Footballers import Footballers
from Playmaker import Playmaker
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSONB



db = SQLAlchemy()

class Users(db.Model):
    __tablename__='Users'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    login=db.Column(db.String,unique=True,nullable=False)
    password = db.Column(db.String, nullable=False)
    rights = db.Column(db.String, nullable=False)

class Playmakers(db.Model):
    __tablename__='Playmakers'

    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String,unique=True,nullable=False)
    lastname = db.Column(db.String, nullable=False)
    league = db.Column(db.String, nullable=False)
    numOfReq = db.Column(db.Integer, )
    data=db.Column(JSONB)
    date=db.Column(db.DateTime,default=datetime.now)

class Leagues(db.Model):
    __tablename__='Leagues'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String,unique=False,nullable=False)
    country=db.Column(db.String,unique=False,nullable=True)