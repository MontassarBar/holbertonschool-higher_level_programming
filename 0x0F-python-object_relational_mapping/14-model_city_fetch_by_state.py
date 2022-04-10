#!/usr/bin/python3
'''prints all City objects from the database hbtn_0e_14_usa'''


import sqlalchemy
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import Base, City
from sys import argv
if __name__ == "__main__":
    engine = sqlalchemy.create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            argv[1], argv[2], argv[3]))

    session = Session(engine)
    obj = session.query(City, State).join(State).order_by(State.id).all()
    for city, state in obj:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
