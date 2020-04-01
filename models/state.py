#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models import storage


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    id = Column(String(60), nullable=False, primary_key=True)

    @state.getter
    def state(self, state_id):
        """Returns the list of Cities with the correspondant state_id
        """
        r = {k: v for k, v in storage.all(City) if v['state_id'] == State.id}
        return(r)
