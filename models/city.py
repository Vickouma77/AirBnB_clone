#!/usr/bin/python3
"""Defines city class"""


class City(BaseModel):
    """Defines the city class

    Attributes:
          state_id: string - empty string: it will be the State.id
          name: string - empty string
    """

    state_id = ""
    name = ""
