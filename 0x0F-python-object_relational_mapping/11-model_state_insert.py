#!/usr/bin/python3
'''adds the State object “Louisiana” to the database hbtn_0e_6_usa'''

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
    obj = State(name='Louisiana')
    session.add(obj)
    session.commit()
    print(obj.id)
    session.close()
