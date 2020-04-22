#!/usr/bin/python3
"""
This is the state class.
"""
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        cascade="all,delete",
        backref="state"
    )

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of Cities with the correspondant state_id
            """
            cities = models.storage.all(City)
            d = {}
            for k, v in cities.items():
                if v.state_id == self.id:
                    d[k] = v
            return(d)
