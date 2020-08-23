from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,IntegerField
from wtforms.validators import InputRequired,Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from wtforms import SelectField

db = SQLAlchemy()

class Room(UserMixin,db.Model):
    __tablename__="room"
    id=db.Column(db.Integer,primary_key=True)
    mate=db.Column(db.String(3))
    number=db.Column(db.Integer)
    
class roomform(FlaskForm):
    mate=SelectField('Room mate ?',choices=[('Y','Yes'),('N','No')],validators=[InputRequired()])
    number=SelectField('How many ?',choices=[],validators=[InputRequired()])
    