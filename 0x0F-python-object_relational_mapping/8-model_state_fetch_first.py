#!/usr/bin/python3
'''prints the first State object from the database hbtn_0e_6_usa'''


import sqlalchemy
from sqlalchemy.orm import Session
from model_state import Base, State
from sys import argv
if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]))
    session = Session(engine)
    result = session.query(State).first()
    if not result:
        print("Nothing")
    else:
        print("{}: {}".format(result.id, result.name))
    session.close()
