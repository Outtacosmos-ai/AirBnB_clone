#!/usr/bin/python3
"""
class Amenity
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class Amenity
    """
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
