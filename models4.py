from flask import Flask,render_template,redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,IntegerField
from wtforms.validators import InputRequired,Length
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user
from wtforms import SelectField

db = SQLAlchemy()

class Choices(UserMixin,db.Model):
    __tablename__="choices"
    id=db.Column(db.Integer,primary_key=True)
    hostel=db.Column(db.String(3))
    type=db.Column(db.String(2))
    sharing=db.Column(db.Integer)

class choiceform(FlaskForm):
    roll=IntegerField('roll number',validators=[InputRequired(),Length(max=9)])
    hostel=SelectField('hostel',choices=[],validators=[InputRequired()])
    type=SelectField('type',choices=[],validators=[InputRequired()])
    sharing=SelectField('sharing',choices=[],validators=[InputRequired()])


