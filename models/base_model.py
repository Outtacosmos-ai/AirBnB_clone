#!/usr/bin/python3
"""
BaseModel is the main model used for all classes
"""
import uuid
import datetime
import models


class BaseModel():
    """
    BaseModel class
    """

    def __init__(self, *_, **kwargs):
        """
        init method
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        iso_format_ = datetime.datetime.fromisoformat(value)
                        setattr(self, key, iso_format_)
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        str return method
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        )

    def save(self):
        """
        save method
        self.__dict__.update({'updated_at': datetime.datetime.now()})
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict method
        """
        diction = dict(self.__dict__)
        diction["__class__"] = self.__class__.__name__
        diction["created_at"] = self.created_at.isoformat()
        diction["updated_at"] = self.updated_at.isoformat()

        return diction
