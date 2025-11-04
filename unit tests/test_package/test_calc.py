import pytest

# This is the same test file as before but now inside a package folder

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
    
# Testing for float inputs, we have to be careful with floating point precision
# Hence, we can use approx from pytest
def test_float():
    # This says that the result should be equal to 6.25 +- 0.0001
    # 1e - 4 means 1 * 10^(-4) = 0.0001
    assert square(2.5) == pytest.approx(6.25, abs=1e-4)
    assert square(-3.1) == pytest.approx(9.61, abs=1e-4)