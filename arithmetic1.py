"""Math functions for calculator."""


def add(num_list):
    """Return the sum of a list of integers"""

    sum = 0

    for i in num_list:
        sum = sum + i

    return int(sum)


def subtract(num1, num2):
    """Return the second number subtracted from the first."""

    return int(num1 - num2)


def multiply(num1, num2):
    """Multiply the two inputs together."""

    return int(num1 * num2)


def divide(num1, num2):
    """Divide the first input by the second, returning a floating point."""

    return float(num1) / num2


def square(num1):
    """Return the square of the input."""

    return int(num1 ** 2)


def cube(num1):
    """Return the cube of the input."""

    return int(num1 ** 3)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""

    return int(num1 ** num2)


def mod(num1, num2):
    """Return the remainder of num1 / num2."""

    return int(num1 % num2)


def add_mult(num1, num2, num3):
    """Adds first two and multiply sum with third"""

    return multiply(add(num1, num2), num3)


def add_cubes(num1, num2):
    """Cubes both numbers and sums them"""

    return add(cube(num1), cube(num2))
