#!/usr/bin/python3
"""
class City
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    class City
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
