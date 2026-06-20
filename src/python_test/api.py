DEFAULT_GREETING = "Hello"


def _normalize_name(name: str) -> str:
    normalized = name.strip()
    return normalized or "friend"


def greet(name: str) -> str:
    return f"{DEFAULT_GREETING}, {_normalize_name(name)}!"


def greet_many(names: list[str]) -> list[str]:
    return [greet(name) for name in names]


def greet_pair(first_name: str, second_name: str) -> tuple[str, str]:
    return (greet(first_name), greet(second_name))
