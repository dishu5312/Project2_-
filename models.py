from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class hostels(db.Model):
    __tablename__="hostel"
    enrolment=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    choice=db.Column(db.String, nullable=False)

class room_type(db.Model):
    __tablename_="room_specs"
    enrolment=db.Column(db.Integer,db.ForeignKey("hostel.enrolment"),primary_key=True)
    ac=db.Column(db.String,nullable=False)
    sharing=db.Column(db.Integer,nullable=False)
    gender=db.Column(db.String,nullable=False)
    room_mate=db.Column(db.String,nullable=False)

