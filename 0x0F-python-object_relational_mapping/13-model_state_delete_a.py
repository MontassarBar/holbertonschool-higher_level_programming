#!/usr/bin/python3
'''deletes all State objects with a name containing
 the letter a from the database hbtn_0e_6_usa'''

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
    for state in session.query(State).order_by(State.id).filter(
            State.name.like('%a%')):
        if 'a' in state.name:
            session.delete(state)
    session.commit()
    session.close()
