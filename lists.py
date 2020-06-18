import os

from flask import Flask,render_template,request
from models import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


def main():
    x=hostels.query.all()
    for hostel in x:
        print(f"student no. {hostel.enrolment} {hostel.name} lives in {hostel.choice}")

if __name__ == "__main__":
    with app.app_context():
        main()
