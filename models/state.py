#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import environ
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City

engine = environ.get("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if (engine == 'db'):
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", back_populates="state")
    else:
        name = ""

    @property
    def cities(self):
        """
        Returns list of city instances
        """
        city_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
