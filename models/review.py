#!/usr/bin/python3
"""
This is the User class module
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    This is Review class that handles review information
    """
    place_id = ""
    user_id = ""
    text = ""
