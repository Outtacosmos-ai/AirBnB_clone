#!/usr/bin/python3
"""
class Review
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    class Review
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
