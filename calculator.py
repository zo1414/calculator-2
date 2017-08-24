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


def calc(opperator, numbers):
    """runs a arthemtic opperation on list of numbers (of any size)"""

    if find_opp(opperator) is None:
        return "Not a valid operator"
    else:
        return reduce(find_opp(opperator), numbers)

#def calc_2(par):
#    """runs arthemtic opperation when only one number"""
#
#    return find_opp(par[0])(int(par[1]))


def flo_inputs(num_list):
    """ chaneges a list in to a list of floats"""

    flo_list = []

    for i in num_list:
        flo_list.append(float(i))
    return flo_list
#   except ValueError:
 #       print "Only numbers after operator accepted"

while True:
    input_string = raw_input(">")
    t_input = input_string.split(" ")
    if t_input[0] == "q":
        print "You are now exiting!"
        break
    else:
        opp = t_input[0]
        try:
            num_list = flo_inputs(t_input[1:])
        except ValueError:
            print "only numbers after operator accepted"
            continue
        print calc(opp, num_list)
        #if len(t_input) < 3:
        #    print calc_2(t_input)
        #else:
        #    print calc_3(t_input)




# Your code goes here
