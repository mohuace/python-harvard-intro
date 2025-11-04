import pytest

# This is a unit test file for calculator.py
# Will be using a tool called pytest to run the tests
from calculator import square

# If we don't use pytest, we will have to define main function to run tests
# Also, need to put try except blocks to catch assertion errors
# And print appropriate messages
# Using pytest, we can simply define test functions and use assert statements
# To run the tests, we just need to run `pytest` command in terminal
def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0
    assert square(5) == 25

# Testing for invalid input, e.g., passing a string instead of a number
def test_str():
    with pytest.raises(TypeError):
        square("cat")