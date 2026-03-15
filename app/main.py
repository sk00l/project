def greet(name: str) -> str:
    """Return a friendly greeting."""
    return f"Hello, {name}!"


def run() -> None:
    name = input("Enter your name: ").strip() or "friend"
    print(greet(name))
    raise RuntimeError("Intentional error: this always fails")


if __name__ == "__main__":
    run()
