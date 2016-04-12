#!/usr/bin/env python3

import sys
import numpy as np


# using a list of tuples because the data will not change and this will provide
# a speed benefit in python. Having the data together also makes it a little
# easier to read.
d = [
    (0.9000, 2.9596),
    (0.9500, 3.0857),
    (1.0000, 3.2183),
    (1.0500, 3.3577),
    (1.1000, 3.5042),
    (1.1500, 3.6582),
    (1.2000, 3.8201),
    (1.2500, 3.9903),
    (1.3000, 4.1693),
    (1.3500, 4.3547),
    (1.4000, 4.5552),
    (1.4500, 4.7631),
    (1.5000, 4.9817),
    (1.5500, 5.2115),
    (1.6000, 5.4530),
    (1.6500, 5.7070),
    (1.7000, 5.9739),
    (1.7500, 6.2546),
    (1.8000, 6.5496),
    (1.8500, 6.8598),
    (1.9000, 7.1859)
]


def eq(a, b):
    # helper to check if two floating points numbers are within a threshold
    if a > (b + 0.00000000001) or a < (b - 0.00000000001):
        return False
    return True


def validate_inputs(data, lb, ub, h):
    lb_index = None
    lb_index = None
    space = data[1][0] - data[0][0]

    if eq(data[0][0], lb):
        lb_index = 0
    if eq(data[0][0], ub):
        ub_index = 0

    for i in range(1, len(data)):
        curr_space = data[i][0] - data[i - 1][0]
        if not eq(curr_space, space):
            print('Invalid Spacing. All datapoints must have the same spacing')
            print('Spacing must be withing +- {0}'.format(THRESHOLD))
            sys.exit(1)

        if eq(data[i][0], lb):
            lb_index = i
        if eq(data[i][0], ub):
            ub_index = i

    if not lb_index and ub_index:
        print('Invalid upper and/or lower bounds. They must fall directly on a datapoint')
        sys.exit(1)

    return (lb_index, ub_index)


def trapezoid(data, lb, ub, h):
    lb_index, ub_index = validate_inputs(data, lb, ub, h)

    x = 0
    x += 0.5 * data[lb_index][1]
    for i in range(1, ub_index - lb_index):
        x += h * data[lb_index + i][1]

    x += 0.5 * data[ub_index][1]

    return abs(x * h)

def simpsonOneThird(data, lb, ub, h):
    lb_index, ub_index = validate_inputs(data, lb, ub, h)
    if ub_index - lb_index < 3:
        print('Need at least 3 data points within the range provided')
        sys.exit(1)

    even = 0
    odd = 0
    for i in range(1, ub_index - lb_index):
        if i % 2 == 0:
            even += data[lb_index + i][1]
        else:
            odd += data[lb_index + i][1]

    x = (h / 6) * (data[lb_index][1] + data[lb_index][1] + (2 * even) + (4 * odd))

    return abs(x)

print('Trapezoid')
print(trapezoid(d, 1.0, 1.8, 0.1))
print(trapezoid(d, 1.0, 1.8, 0.2))
print()
print('Simpson\'s 1/3')
print(simpsonOneThird(d, 1.0, 1.8, 0.1))
print(simpsonOneThird(d, 1.0, 1.8, 0.2))
