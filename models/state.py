#!/usr/bin/python3
"""Defining the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class.

    Attributes:
           name(str): name of the state
    """

    name = ""
