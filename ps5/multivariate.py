#!/usr/bin/env python3

import math
import numpy
from operator import add

TOLERANCE = 0.000001
MAX_TRIES = 100

# Lots of helper functions to clear up whats happening.


def fu(vec):
    return (2 * math.pow(vec[0], 2) + -4 * vec[0] + math.pow(vec[1], 2)
            + 3 * math.pow(vec[2], 2) + 6 * vec[2] + 2)


def fv(vec):
    return (math.pow(vec[0], 2) + math.pow(vec[1], 2) - 2 * vec[1]
            + 2 * math.pow(vec[2], 2) - 5)


def fw(vec):
    return (3 * math.pow(vec[0], 2) - 12 * vec[0] + math.pow(vec[1], 2)
            + 3 * math.pow(vec[2], 2) + 8)


def du(vec):
    return [(4 * vec[0]) - 4, (2 * vec[1]), (6 * vec[2]) + 6]


def dv(vec):
    return [(2 * vec[0]), (2 * vec[1]) - 2, (4 * vec[2])]


def dw(vec):
    return [(6 * vec[0]) - 12, (2 * vec[1]), (6 * vec[2])]


iteration = 0
vector = [1.0, 1.0, 1.0]

print("{0:<12} {1:<7} {2:<7} {3:<7}".format("iteration", "u", "v", "w"))

# Main logic for Multivariate Newton's method
while (iteration < MAX_TRIES):
    f = [
        -1 * fu(vector),
        -1 * fv(vector),
        -1 * fw(vector)
    ]

    df = [
        du(vector),
        dv(vector),
        dw(vector)
    ]

    # uses numpy to solve the matrix, unsure if our previous gaussian solver
    # was correct.
    solution = numpy.linalg.solve(df, (f))

    if (abs(solution[0]) < TOLERANCE) and (abs(solution[1]) < TOLERANCE) \
            and (abs(solution[2]) < TOLERANCE):
        print('Finished in {0} iterations'.format(iteration))
        print('{0:<12} {1:<7.3f} {2:<7.3f} {3:<7.3f}'.format(
            iteration, vector[0], vector[1], vector[2]))
        break

    iteration += 1

    # add two arrays together
    vector = list(map(add, vector, solution))
    print('{0:<12} {1:<7.3f} {2:<7.3f} {3:<7.3f}'.format(
        iteration, vector[0], vector[1], vector[2]))

print('done')


'''
###output of the above function###
iteration    u       v       w
1            -2.833  -20.000 3.667
2            -0.959  -9.700  1.845
3            0.064   -4.742  0.741
4            0.659   -2.448  0.134
5            0.971   -1.488  -0.154
6            1.081   -1.196  -0.249
7            1.096   -1.160  -0.261
8            1.096   -1.159  -0.261
Finished in 8 iterations
8            1.096   -1.159  -0.261
'''
