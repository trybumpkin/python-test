def greet(name: str) -> str:
    return f"Hello, {name}!"


def greet_many(names: list[str]) -> list[str]:
    return [greet(name) for name in names]
