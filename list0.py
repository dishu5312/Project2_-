import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(os.getenv('DATABASE_URL'))
db=scoped_session(sessionmaker(bind=engine))

def main():
    hostels = db.execute("SELECT id,name,choice FROM hostels")
    for hostel in hostels:
        print(f"{hostel.id} number student {hostel.name} lives in hostel {hostel.choice}")

if __name__ == "__main__":
    main()