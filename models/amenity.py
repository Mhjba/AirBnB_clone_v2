#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import so

class Amenity(BaseModel, Base):
    """ The Amenity Class """
    __tablename__ = 'amenities'
    if so.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

    else:
        name = ""
