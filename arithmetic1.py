"""Math functions for calculator."""


def add(num_list):
    """Return the sum of a list of integers"""

    sum = 0

    for i in num_list:
        sum = sum + i

    return int(sum)


def subtract(num_list):
    """Return the difference of a list of integers"""

    diff = 0

    for i in num_list:
        diff = diff - i

    return int(diff)


def multiply(num_list):
    """Return the product of a list of integers"""

    pro = 1

    for i in num_list:
        pro = pro * i

    return int(pro)


def divide(num_list):
    """Divide the first input by the second, returning a floating point."""

    quo = num_list[0]

    for i in num_list[1:]:
        quo = quo / i
    return quo


def square(num_list):
    """Return a list of squares from a list."""

    squ_list = []

    for i in num_list:
        squ_list.append(i ** 2)
    return squ_list


def cube(num_list):
    """Return a list of cubes of a list."""

    cube_list = []

    for i in num_list:
        cube_list.append(i ** 3)

    return cube_list


def power(num_list):
    """Takes a list of numbers and sequentially raises each to the power of the next"""

    raised = num_list[0]

    for i in num_list[1:]:
        raised = raised ** i

    return raised


def mod(num_list):
    """Takes a list and sequentially modulates."""

    rem = num_list[0]

    for i in num_list[1:]:
        rem = rem % i

    return rem


def add_mult(num1, num2, num3):
    """Adds first two and multiply sum with third"""

    return multiply(add(num1, num2), num3)


def add_cubes(num1, num2):
    """Cubes both numbers and sums them"""

    return add(cube(num1), cube(num2))
