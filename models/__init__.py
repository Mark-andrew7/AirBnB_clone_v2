#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from os import getenv
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.review import Review

dummy_classes = {"BaseModel": BaseModel, "User": User,
                 "Review": Review, "City": City,
                 "State": State, "Place": Place,
                 "Amenity": Amenity}

storage_engine = getenv('HBNB_TYPE_STORAGE')

if storage_engine == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
