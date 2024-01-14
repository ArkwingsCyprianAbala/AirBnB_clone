#!/usr/bin/python3
"""
This is the User class module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    This is User class that handles user's information
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
