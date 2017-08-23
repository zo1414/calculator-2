"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *


def find_opp(opp):
    if opp == "+":
        return add
    elif opp == "-":
        return subtract
    elif opp == "*":
        return multiply
    elif opp == "/":
        return divide
    elif opp == "square":
        return square
    elif opp == "cube":
        return cube
    elif opp == "pow":
        return power
    elif opp == "mod":
        return mod


def calc_3(par):
    """runs a arthemtic opperation on two numbers"""

    return find_opp(par[0])(int(par[1]), int(par[2]))


def calc_2(par):
    """runs arthemtic opperation when only one number"""

    return find_opp(par[0])(int(par[1]))


while True:
    input_string = raw_input(">")
    t_input = input_string.split(" ")
    if t_input[0] == "q":
        print "You are now exiting!"
        break

    else:
        if len(t_input) < 3:
            print calc_2(t_input)
        else:
            print calc_3(t_input)




# Your code goes here
