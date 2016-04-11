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


def validate_inputs(data, lower_bound, upper_bound, h):
    valid_lb = False
    valid_ub = False
    space = data[1][0] - data[0][0]

    if eq(data[0][0], lower_bound):
        valid_lb = True
    if eq(data[0][0], upper_bound):
        valid_ub = True

    for i in range(1, len(data)):
        curr_space = data[i][0] - data[i - 1][0]
        if not eq(curr_space, space):
            print('Invalid Spacing. All datapoints must have the same spacing')
            print('Spacing must be withing +- {0}'.format(THRESHOLD))
            sys.exit(1)

        if eq(data[i][0], lower_bound):
            valid_lb = True
        if eq(data[i][0], upper_bound):
            valid_ub = True

    if not valid_lb and valid_ub:
        print('Invalid upper and/or lower bounds. They must fall directly on a datapoint')
        sys.exit(1)


def trapezoid(data, lower_bound, upper_bound, h):
    validate_inputs(data, lower_bound, upper_bound, h)

trapezoid(d, 1.0, 1.8, 0.1)
