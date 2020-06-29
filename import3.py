import os
import csv

from flask import Flask,render_template,request
from models2 import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

def main():
    f=open("gender.csv")
    reader=csv.reader(f)
    for number,gender,hostel in reader:
        hostel=Hostels(number=number,gender=gender,hostel=hostel)
        db.session.add(hostel)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()