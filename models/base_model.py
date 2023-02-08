#!/usr/bin/python3
"""defines the BaseModel class"""

import datetime
import uuid
import string


class BaseModel:
    """BaseModel for the project"""

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel.

        Args:
            *args: not used.
            **kwargs(dict): key/value pairs of attributes.
        """
