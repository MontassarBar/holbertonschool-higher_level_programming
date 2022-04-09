#!/usr/bin/python3
'''state class'''


from sqlalchemy import Column, Integer, String, column
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    '''the class definition of a State'''

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
