#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(String(60), nullable=False, primary_key=True)
    cities = relationship(
        "City",
        cascade="all,delete",
        backref="state",
    )

    @property
    def cities(self, state_id):
        """Returns the list of Cities with the correspondant state_id
        """
        cities = models.storage.all(City)
        d = {}
        for k, v in cities.items():
            if v.state_id == cls.id:
                d[k] = v
        return(d)
