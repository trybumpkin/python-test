DEFAULT_FAREWELL = "Goodbye"


def farewell(name: str) -> str:
    cleaned_name = name.strip()
    return f"{DEFAULT_FAREWELL}, {cleaned_name or 'friend'}!"
