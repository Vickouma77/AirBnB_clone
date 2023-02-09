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
