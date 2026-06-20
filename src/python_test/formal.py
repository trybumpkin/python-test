def greet_formally(title: str, name: str) -> str:
    cleaned_title = title.strip().rstrip(".")
    cleaned_name = name.strip()
    return f"Hello, {cleaned_title}. {cleaned_name}!"
