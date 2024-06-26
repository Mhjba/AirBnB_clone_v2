#!/usr/bin/python3
"""This module instantiates an object of DBStorage or FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

if os.getenv('HBNB_TYPE_STORAGE') == 'db':
    """ Unique FileStorage/DBStorage for all models """
    storage = DBStorage()

else:

    storage = FileStorage()
storage.reload()
