#!/usr/bin/python3
"""
Database storage
"""

from os import environ, getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import models

HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')


class DBStorage():
    """
    Database storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initialize db
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB), pool_pre_ping=True
                                      )

        env = getenv('HBNB_ENV')
        if (env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on current db session
        """
        obj_dict = {}
        if cls:
            for clas in cls:
                objects = self.__session.query(clas).all()
                for obj in objects:
                    key = '{}.{}'.format(obj.__class__.__name__, obj.id)
                    obj_dict[key] = obj
            return obj_dict

    def new(self, obj):
        """
        add the object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in database
        """
        Base.metadata.create_all(self.__engine)
        Session = session.maker(bind=self.__engine, expire_on_commit=False)
        scoped = scoped_session(Session)
        self.__session = scoped
