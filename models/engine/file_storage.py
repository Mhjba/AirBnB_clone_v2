#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.

    Attributes:
        path (str): The name of the file to save objects to.
        obj (dict): A dictionary of instantiated objects.
    """
    path = "file.json"
    obj = {}

    def all(own):
        """Return the dictionary."""
        return FileStorage.obj

    def new(own, obj):
        """Set in obj obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.obj["{}.{}".format(ocname, obj.id)] = obj

    def save(own):
        """Serialize obj to the JSON file path."""
        odict = FileStorage.obj
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.path, "w") as f:
            json.dump(objdict, f)

    def reload(own):
        """Deserialize the JSON file path to obj, if it exists."""
        try:
            with open(FileStorage.path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    own.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
