import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField ,IntegerField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms import SelectField


  # Import table definitions.
from models4 import *

app = Flask(__name__)

  # Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:567890@localhost:5432/project"
#os.getenv("DATABASE_URl")#os.getenv("postgres://postgres:567890@localhost:5432/project")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  # Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)

def main():
      # Create tables based on each table definition in `models`
    db.create_all()

if __name__ == "__main__":
      # Allows for command line interaction with Flask application
    with app.app_context():
        main()