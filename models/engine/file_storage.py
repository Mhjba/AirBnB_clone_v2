#!/usr/bin/python3
"""Defines the FileStorage class."""
import json

class FileStorage:

    """This class manages storage of hbnb models in JSON format"""
    __path = "file.json"
    __objs = {}

    def all(self):
        """Return the dictionary."""
        return FileStorage.__objs

    def new(self, obj):
        """Set in obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objs["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to the JSON file path"""
        o_dict = FileStorage.__objs
        o_dic = {obj: o_dict[obj].to_dict() for obj in o_dict.keys()}
        with open(FileStorage.__path, "w") as file:
            json.dump(o_dic, file)

    def reload(self):
        """Deserialize the JSON file path to obj, if it exists."""
        try:
            with open(FileStorage.__path) as file:
                o_dict = json.load(file)
                for key in o_dict.values():
                    name = key["__class__"]
                    del key["__class__"]
                    self.new(eval(name)(**key))
        except FileNotFoundError:
            return

    def delete(self, obj=None):
        """reload objects"""
        if obj is None: 
                        return
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        if key in FileStorage.__objs:
            del FileStorage.__objs[key]
            self.save()

    def close(self):
        """ Reload objects """
        self.reload()
