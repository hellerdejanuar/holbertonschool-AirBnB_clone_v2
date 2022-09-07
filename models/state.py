#!/usr/bin/python3
""" State Module for HBNBZZz project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        cities = relationship("City", backref="state", cascade="all, \
                              delete-orphan")
    else:
        @property
        def cities(self):
            """ getter that returns cities linked to current state """
            from models import storage
            cities_list = []
            for cit in storage.all(City).values():
                if self.id == cit.state_id:
                    cities_list.append(cit)
            return cities_list
