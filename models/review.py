#!/usr/bin/python3
''' Review module for the HBNB project '''
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Text, ForeignKey
from os import getenv


class Review(BaseModel, Base):
    ''' The Review class '''
    __tablename__ = 'reviews'

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        text = Column(Text(1024), nullable=False)
        place_id = Column(String(60),
                          ForeignKey('places.id', ondelete='CASCADE'),
                          nullable=False)
        user_id = Column(String(60),
                         ForeignKey('users.id', ondelete='CASCADE'),
                         nullable=False)
    else:
        text = ''
        place_id = ''
        user_id = ''
