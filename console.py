#!/usr/bin/python3
"""Defines HBnB console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.
    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }
