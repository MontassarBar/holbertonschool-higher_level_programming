#!/usr/bin/python3
'''changes the name of a State object from the database hbtn_0e_6_usa'''

from unicodedata import name
import sqlalchemy
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv
if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]))
    session = Session(engine)
    obj = session.query(State).get(2)
    obj.name = 'New Mexico'
    session.commit()
    session.close()
