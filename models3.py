from flask import Flask, render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,IntegerField
from wtforms.validators import InputRequired,Email,Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from wtforms import SelectField

db=SQLAlchemy()

class Hotels(db.Model):
    __tablename__="hotels"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(3),nullable=False)
    type = db.Column(db.String(1),nullable=False)
    sharing = db.Column(db.Integer)
    gender = db.Column(db.String(1))

