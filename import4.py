import os
import csv

from flask import Flask,render_template,request
from models3 import *

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATION"]=False
db.init_app(app)

def main():
    f=open("hosteld.csv")
    reader=csv.reader(f)
    for id,name,type,sharing,gender in reader:
        hotels=Hotels(id=id,name=name,type=type,sharing=sharing,gender=gender)
        db.session.add(hotels)
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        main()