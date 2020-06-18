import csv
fName = "aFile.csv"

try:
    with open(fName, 'rb') as f:
        reader = csv.reader(f)
        for row in reader:
            pass #do stuff here

except IOError:
    print("Could not read file:", fName)

import os

from flask import Flask,render_template,request
from models import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)

def main():
    f = open("hostel.csv")
    reader = csv.reader(f)
    for enrolment, name, choice in reader:
        hostel=hostels(enrolment=enrolment, name=name, choice=choice)
        db.session.add(hostel)
        print(f"student number {enrolment} added {name} in {choice} ")
        db.session.commit()

if __name__== "__main__":
    with app.app_context():
        main()        
