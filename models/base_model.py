#!/usr/bin/python3
"""defines the BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """BaseModel for the project"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel.

        Args:
            *args: not used.
            **kwargs(dict): key/value pairs of attributes.
        """

        form_t = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.todat()

        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                     self.__dict__[key] = datetime.strptime(value, form_t)
                 else:
                     self.__dict__[key] = value


    def save(self):
        """updates the public instance attribute updated_at with the current datetime"""
        self.updated_at = datetime.today()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
