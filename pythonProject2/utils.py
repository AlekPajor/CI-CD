"""
This module provides basic arithmetic operations.

Functions:
    - add(a: int, b: int) -> int: Returns the sum of two integers.
    - subtract(a: int, b: int) -> int: Returns the difference between two integers.
    - multiply(a: int, b: int) -> int: Returns the product of two integers.
    - divide(a: int, b: int) -> float: Returns the quotient of two integers.
"""

def add(a: int, b: int) -> int:
    """
    Adds two integers.

    Parameters:
    a (int): The first integer to add.
    b (int): The second integer to add.

    Returns:
    int: The sum of the two integers.
    """
    return a + b


def subtract(a: int, b: int) -> int:
    """
    Subtracts the second integer from the first integer.

    Parameters:
    a (int): The integer to be subtracted from.
    b (int): The integer to subtract.

    Returns:
    int: The difference between the two integers.
    """
    return a - b


def multiply(a: int, b: int) -> int:
    """
    Multiplies two integers.

    Parameters:
    a (int): The first integer to multiply.
    b (int): The second integer to multiply.

    Returns:
    int: The product of the two integers.
    """
    return a * b


def divide(a: int, b: int) -> float:
    """
    Divides the first integer by the second integer.

    Parameters:
    a (int): The integer to be divided.
    b (int): The integer to divide by.

    Returns:
    float: The quotient of the division.
    """
    return a / b
