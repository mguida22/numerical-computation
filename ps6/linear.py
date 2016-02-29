#!/usr/bin/env python3

point_a = (1, 1)
point_b = (5, 5)

def interpolate(a, b, x):
    # point-slope formula
    m = (b[1] - a[1]) / (b[0] - a[0])
    return (m * (x - a[0]) + a[1])

y = interpolate(point_a, point_b, 3)
print(y)
