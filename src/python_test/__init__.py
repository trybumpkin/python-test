from .api import DEFAULT_GREETING, greet, greet_many, greet_pair, greet_with_prefix
from .catalog import available_greetings
from .formal import greet_formally

__all__ = [
    "DEFAULT_GREETING",
    "greet",
    "greet_many",
    "greet_pair",
    "greet_with_prefix",
    "available_greetings",
    "greet_formally",
]
