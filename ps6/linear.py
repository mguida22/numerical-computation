#!/usr/bin/env python3

# data from http://physics.bu.edu/~redner/projects/population/cities/newyork.html

import matplotlib.pyplot as plt

population = [
    (1790, 33131),
    (1800, 60515),
    (1810, 96373),
    (1820, 123706),
    (1830, 202589),
    (1840, 312710),
    (1850, 515547),
    (1860, 813669),
    (1870, 942292),
    (1880, 1206299),
    (1890, 1515301),
    (1900, 3437202),
    (1910, 4766883),
    (1920, 5620048),
    (1930, 6930446),
    (1940, 7454995),
    (1950, 7891957),
    (1960, 7781984),
    (1970, 7894862),
    (1980, 7071639),
    (1990, 7322564)
]

# plot data
plt.scatter(*zip(*population))
plt.title('NYC Population by Decade')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

# interpolate using data
def interpolate(a, b, x):
    # point-slope formula
    m = (b[1] - a[1]) / (b[0] - a[0])
    return (m * (x - a[0]) + a[1])

y = interpolate(population[-2], population[-1], 1985)
print(y)