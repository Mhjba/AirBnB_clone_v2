#!/usr/bin/python3
''' State Module for HBNB project '''
from models import storage
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    ''' The State class '''
    __tablename__ = 'states'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all, delete")
    else:
        name = ''

        @property
        def cities(self):
            '''Retrieve all cities associated with this state'''
            dict_objs = storage.all(City)
            state_cities = []

            for city in dict_objs.values():
                if city.state_id == self.id:
                    state_cities.append(city)

            return state_cities
