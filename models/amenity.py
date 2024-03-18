#!/usr/bin/python3
""" Amenity Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import os


class Amenity(BaseModel, Base):
    """The Amenity Class"""
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)

    else :
        nume = ''

