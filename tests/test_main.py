from app.main import greet


def test_greet() -> None:
    assert greet("Ada") == "Hello, Ada!"
