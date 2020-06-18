import os
import csv

from flask import Flask,render_template, request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

def main():
    f=open("room_type.csv")
    reader=csv.reader(f)
    for enrolment,ac,sharing,gender,room_mate in reader:
        room=room_type(enrolment=enrolment,ac=ac,sharing=sharing,gender=gender,room_mate=room_mate)
        db.session.add(room)
        print(f"{enrolment} have chosen a {sharing} sharing room with {ac} is a {gender} with {room_mate} roommate ")
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()