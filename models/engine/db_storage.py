#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place, place_amenity
from models.amenity import Amenity
from models.review import Review
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in a SQL database"""
    __engine = None
    __session = None
    o_dct = dict()
    my_cls = (User, State, City, Amenity, Place, Review)

    def __init__(self):
        """Initializes the SQL database storage"""
        user = getenv('HBNB_MYSQL_USER')
        pword = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(user, pword, host, db_name)
        self.__engine = create_engine(DATABASE_URL,
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Method to return a dictionary of objects"""
        my_cls = {}
        o_dct = {}
        if cls is None:
            for class_type in my_cls:
                query = self.__session.query(class_type)
                for obj in query.all():
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    o_dct[key] = obj
        else:
            query = self.__session.query(cls)
            for obj in query.all():
                key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                o_dct[key] = obj
        return o_dct


    def new(self, obj):
        """Method to add a new object to the current database"""
        self.__session.add(obj)

    def reload(self):
        """Loads storage database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def save(self):
        """Commits the session changes to database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Commits the session changes to database"""
        self.__session.delete(obj)

    def close(self):
        """Closes the storage engine."""
        self.__session.close()
