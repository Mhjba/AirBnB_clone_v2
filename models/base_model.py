#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def __init__(own, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        test_form = "%Y-%m-%dT%H:%M:%S.%f"
        own.id = str(uuid4())
        own.created_at = datetime.today()
        own.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    own.__dict__[k] = datetime.strptime(v, test_form)
                else:
                    own.__dict__[k] = v
        else:
            models.storage.new(own)

    def save(own):
        """Update updated_at with the current datetime."""
        own.updated_at = datetime.today()
        models.storage.save()

    def to_dict(own):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair __class__ representing
        the class name of the object.
        """
        rdi = own.__dict__.copy()
        rdi["created_at"] = own.created_at.isoformat()
        rdi["updated_at"] = own.updated_at.isoformat()
        rdi["__class__"] = own.__class__.__name__
        return rdi

    def __str__(own):
        """Return the print/str representation of the BaseModel instance."""
        clname = own.__class__.__name__
        return "[{}] ({}) {}".format(clname, own.id, own.__dict__)
