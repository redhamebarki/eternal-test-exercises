"""Implémenter find_largest et find_absolute_largest

Coverage 100%. Les tests doivent passer. Des docstrings doivent être présentes
"""
import pytest

def find_largest(numbers: list):
    # Check if the input is actually a list and it is not empty
    if not isinstance(numbers, list) or not numbers:
        raise ValueError("Input must be a non-empty list")

    # Ensure all elements in the list are numbers (int or float)
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")

    # Finding the largest number using max function
    return max(numbers)





def find_absolute_largest(numbers: list):
    if not isinstance(numbers, list) or not numbers:
        raise ValueError("Input must be a non-empty list")

    # Ensure all elements in the list are numbers (int or float)
    if not all(isinstance(num, (int, float)) for num in numbers):
        raise ValueError("All elements must be numbers")
    return max(numbers,key=abs)

def test_find_largest():
    assert find_largest([0, 1, 2, 3, 40]) == 40
    assert find_largest([40, 3, 2, 1, 0]) == 40
    assert find_largest([4, -100, 2]) == 4
    with pytest.raises(ValueError):
        find_largest([1, 2, 3, 'z'])
    with pytest.raises(ValueError):
        find_largest(42)

def test_find_absolute_largest():
    assert find_absolute_largest([0, 1, 2, 3]) == find_largest([0, 1, 2, 3])
    assert find_absolute_largest([-1, -2, -3, -4]) == - find_absolute_largest([1, 2, 3, 4])
    assert find_absolute_largest([1, 2, 3, -100]) == -100
    assert find_absolute_largest([-100, 200, -300, 400, -500, 10]) == -500
    with pytest.raises(ValueError):
        find_absolute_largest([1, 2, 3, 'z'])
    with pytest.raises(ValueError):
        find_absolute_largest(42)