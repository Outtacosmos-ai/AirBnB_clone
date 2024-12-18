#!/usr/bin/python3
"""
class User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
