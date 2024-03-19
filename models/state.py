#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
    else:
        name = ''

    @property
    def cities(self):
        """getter attribute cities that returns the list of City"""
        from models import storage
        cities_state = []
        my_cities = storage.all(City).values()
        for value in my_cities:
            if self.id == value.state_id:
                cities_state.append(value)
        return cities_state
