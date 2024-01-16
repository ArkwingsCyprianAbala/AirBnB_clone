#!/usr/bin/python3
"""
This is the User class module
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    This is City class that handles city's information
    """
    state_id = ""
    name = ""
