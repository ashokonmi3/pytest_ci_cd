import pytest


def test_addition():
    result = add(2, 3)
    assert result == 5


def test_subtraction():
    result = subtract(10, 3)
    assert result == 7, f"Expected 7 but got {
        result}"  # execute in failed case


def test_list_contents():
    fruits = ["apple", "banana", "cherry"]
    assert "apple" in fruits
    assert len(fruits) == 3


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_zero_division_with_message():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(1, 0)


def test_float_comparison():
    assert (0.1 + 0.2) == pytest.approx(0.3)


def test_multiple_assertions():
    assert 1 + 1 == 2
    assert 2 * 2 == 4
    assert 3 - 1 == 2


def test_string_contains():
    greeting = "Hello, World!"
    assert "Hello" in greeting

# File naming convention : prefix or sufix with test_ _test
# login_test.py
# test_login.py
# test_calculator.py
# user_test.py

# function naming convention
# test_

# Class
# TestCalculator

# Othe than convention
# pytest my_custom_test_file.py
# pytest path/to/your_file.py


# Assertion                    |	Description                           |	Example
# Equality Check               |	Checks if two values are equal                     | assert x == 5
# Inequality Check             |	Checks if two values are not equal                 | assert x != y
# Membership Check             |	Checks if a value is in a collection               | assert "apple" in fruits
# Exception Check              |	Asserts that a function raises a specific exception| with pytest.raises(ValueError): my_func()
# Approximation(Floating Point)|	Asserts with small tolerance for floats            | assert (0.1 + 0.2) == pytest.approx(0.3)
# Length Check                 | 	Asserts length of a collection                     | assert len(my_list) == 5
