"""Unit tests for the add.py module."""

def test_add_function():
    """Test the add function with valid inputs."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0
