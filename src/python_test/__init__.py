from .api import DEFAULT_GREETING, greet, greet_many, greet_pair
from .catalog import available_greetings
from .formal import greet_formally
from .farewell import DEFAULT_FAREWELL, farewell

__all__ = [
    "DEFAULT_GREETING",
    "greet",
    "greet_many",
    "greet_pair",
    "available_greetings",
    "greet_formally",
    "DEFAULT_FAREWELL",
    "farewell",
]
