#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models import city

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", back_populates="state", cascade="all, delete-orphan"
            )
    @property
    def cities(self):
        """ returns the list of City object
            with the same id as State
        """
        city_list = []
        city_objects = storage.all(city.City)
        for instance in city_objects:
            if instance == self.id:
                city_list.append(instance)
        return city_list
