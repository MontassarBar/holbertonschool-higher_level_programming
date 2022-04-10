#!/usr/bin/python3
''' prints the State object with the name passed as argument
 from the database hbtn_0e_6_usa'''


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
    x = 0
    for state in session.query(State).order_by(State.id).all():
        if argv[4] == state.name:
            print(state.id)
            x += 1
    if x != 1:
        print("Not found")
    session.close()
