"""
 Author: Aidan Kiser
 Version: 11 Septemeber 2024
"""

def fizzBuzz(value):
    if isMultiple(value, 3):
        return "Fizz"
    if isMultiple(value, 5):
        return "Buzz"
    return str(value)

# UM-02: is multiple utility method to check if a number is a multiple of another
def isMultiple(value, mod):
    """
    Checks if value is a multiple of mod.

    Args:
        value (int): The value to be checked.
        mod (int): The modulus to check against.

    Returns:
        bool: True if value is a multiple of mod, False otherwise.
    """
    return value % mod == 0

def checkFizzBuzz(value, expectedRetVal):
    """
    Checks if a given value meets the FizzBuzz rules.

    Args:
        value (int): The number to be checked.
        expectedRetVal (str): The expected return value based on the FizzBuzz rules.

    Returns:
        bool: True if the value matches the expected return value, False otherwise.
    """

    """Validate whether the FizzBuzz function returns the expected result given an input value."""
    actualRetVal = fizzBuzz(value)
    assert str(actualRetVal) == str(expectedRetVal), \
        f"Expected {expectedRetVal}, but got {actualRetVal} for input: {value}"
