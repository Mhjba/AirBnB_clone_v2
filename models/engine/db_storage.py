#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb clone"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """This class manages database storage of hbnb models in MySQL DB"""
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the SQL database storage"""
        user = getenv('HBNB_MYSQL_USER')
        pword = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        DATABASE_URL = "mysql+mysqldb://{}:{}@{}:3306/{}".format(
            user, pword, host, db_name)
        self.__engine = create_engine(DATABASE_URL,
                                      pool_pre_ping=True)
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        all_dict = {}
        if cls in self.__classes:
            obj = DBStorage.__session.query(cls)
            for i in obj:
                key = "{}.{}".format(i.__class__.__name__, i.id)
                all_dict[key] = i
        elif cls is None:
            for cl in self.__classes:
                ojb = DBStorage.__session.query(cl)
                for i in obj:
                    key = "{}.{}".format(i.__class__.__name__, i.id)
                    all_dict[key] = i
        return all_dict

    def delete(self, obj=None):
        """Removes an object from the storage database"""
        if obj is not None:
            self.__session.delete(obj)

    def new(self, obj):
        """Adds new object to storage database"""
        self.__session.commit(obj)


    def save(self):
        """Commits the session changes to database"""
        self.__session.commit()

    def reload(self):
        """Loads storage database"""
        Base.metadata.create_all(self.__engine)
        rel_Session = sessionmaker(bind=self.__engine,
                                   expire_on_commit=False)
        
        self.__session = scoped_session(rel_Session)()

    def close(self):
        """Closes the storage engine"""
        self.__session.close()
