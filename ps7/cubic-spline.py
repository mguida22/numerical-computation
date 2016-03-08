#!/usr/bin/env python3

a = [1, 2, 3, 4, 5, 6, 7]
b = [1, 3, 2, 1, 2, 4, 5]

def pprint(m):
    for row in m:
        print(row)

# calc coeffs
def splinecoeff(x, y):
    # length of x
    n = 7

    A = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    r = [0, 0, 0, 0, 0, 0, 0]

    dx = []
    dy = []
    for i in range(0, n-2):
        dx[i] = x[i+1] - x[i]
        dy[i] = y[i+1] - y[i]

    for i in range(1, n-2):
        A[i][]

splinecoeff(a, b)
