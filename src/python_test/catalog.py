from .api import DEFAULT_GREETING


def available_greetings() -> list[str]:
    return [DEFAULT_GREETING, "Howdy", "Welcome"]
