#!/usr/bin/python3
'''city class'''


from sqlalchemy import Column, Integer, String, Column, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    '''the class definition of a City'''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, unique=True, nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
