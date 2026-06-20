DEFAULT_GREETING = "Hello"


def greet(name: str) -> str:
    return f"{DEFAULT_GREETING}, {name}!"


def greet_many(names: list[str]) -> list[str]:
    return [greet(name) for name in names]
