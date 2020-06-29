from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Hostels(db.Model):
    __tablename__="hostels"
    number=db.Column(db.Integer, primary_key=True)
    gender=db.Column(db.String, nullable=False)
    hostel=db.Column(db.String, nullable=False)