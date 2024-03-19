#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from os import getenv

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ The Place class """
    __tablename__ = "places"
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref='place', cascade="all, delete")
        amenities = relationship("Amenity", secondary=place_amenity,
                             viewonly=False)

    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []
    @property
    def reviews(self):
        """Retrieve all reviews associated with this place """
        from models import storage
        my_rev = []
        all_reviews = storage.all('Review').values()
        for review in all_reviews:
            if self.id == review.place_id:
                my_rev.append(review)
        return my_rev

    @property
    def amenities(self):
        """ Contains all Amenity """
        from models import storage
        my_amen = []
        all_amenities = storage.all('Amenity').values()
        for amenity in all_amenities:
            if self.id == amenity.amenity_ids:
                my_amen.append(amenity)
        return my_amen

    @amenities.setter
    def amenities(self, obj):
        """ Retrieve all reviews associated with this place """
        if isinstance(obj, 'Amenity'):
            self.amenity_id.append(obj.id)
