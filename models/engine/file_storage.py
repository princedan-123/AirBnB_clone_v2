#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models of cls currently in storage"""
        all_objects = FileStorage.__objects

        if cls:
            cls_objects = {}
            for key, obj in all_objects.items():
                if key[:key.find('.')] == cls.__name__:
                    cls_objects[key] = obj
            return cls_objects
        else:
            return all_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.all().update({key:obj})

    def delete(self, obj=None):
        """Deletes an object from the storage dictionary"""
        if obj:
            key = obj.to_dict()['__class__'] + '.' + obj.id
            del FileStorage.__objects[key]

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except Exception:
            # Either FileNotFound or JSONDecodeError when
            # the file exist, but nothing is inside
            pass

    def close(self):
        """Deserializes JSON to objects."""
        reload()
