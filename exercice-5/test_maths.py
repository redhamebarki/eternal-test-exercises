import pytest


def add(x, y):
    """Addition function."""
    return x + y

def subtract(x, y):
    """Subtraction function."""
    return x - y

def multiply(x, y):
    """Multiplication function."""
    return x * y

def divide(x, y):
    """Division function."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

"""écrire les tests unitaires pour ces fonctions.
atteindre un coverage de 100%
"""

def test_add():
    assert add(5,2) == 7
def test_subtract():
    assert subtract(5,2) == 3
def test_multiply():
    assert multiply(5,2) == 10
def test_divide():
    
    with pytest.raises(ValueError) as e:
        divide(10, 0)
    assert str(e.value) == "Cannot divide by zero!"
    assert divide(10,2) == 5
    assert divide(5,2) == 2.5