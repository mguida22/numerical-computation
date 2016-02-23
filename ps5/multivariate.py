# !/usr/bin/env python3

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

    solution = numpy.linalg.solve(df, (f))

    if (abs(solution[0]) < TOLERANCE) and (abs(solution[1]) < TOLERANCE) \
        and (abs(solution[2]) < TOLERANCE):
            print('Finished in {0} iterations'.format(iteration))
            print('{0:.4f}  {1:.4f}  {2:.4f}'.format(vector[0], vector[1], vector[2]))
            break

    iteration += 1

    # add two arrays together
    vector = list(map(add, vector, solution))
    print('{0}: {1:.4f} {2:.4f} {3:.4f}'.format(iteration, vector[0], vector[1], vector[2]))

print('done')
