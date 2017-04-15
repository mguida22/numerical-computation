#!/usr/bin/env python3

# data from
# http://physics.bu.edu/~redner/projects/population/cities/newyork.html

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

print("close the plot window to run the rest of the code")

# plot data
plt.scatter(*zip(*population))
plt.title('NYC Population by Decade')
plt.xlabel('Year')
plt.ylabel('Population')
plt.show()

print()

# interpolate using (1980,1990) for 1985


def interpolate(a, b, x):
    # point-slope formula
    m = (b[1] - a[1]) / (b[0] - a[0])
    return (m * (x - a[0]) + a[1])

y = interpolate(population[-2], population[-1], 1985)
print("The interpolate estimate for population in 1985 is {0}".format(y))
# interpolate using (1790,1990) for 2050
y = interpolate(population[0], population[-1], 2050)
print("The extrapolate estimate for population in 2050 is {0}".format(y))


def lagrange(a, b, c, x):
    # lagrange equation from textbook
    t1 = a[1] * (((x - b[0]) * (x - c[0])) / ((a[0] - b[0]) * (a[0] - c[0])))
    t2 = b[1] * (((x - a[0]) * (x - c[0])) / ((b[0] - a[0]) * (b[0] - c[0])))
    t3 = c[1] * (((x - a[0]) * (x - b[0])) / ((c[0] - a[0]) * (c[0] - b[0])))

    return (t1 + t2 + t3)

y = lagrange(population[-3], population[-2], population[-1], 1985)
print("The Lagrangian estimate for population in 2050 is {0}".format(y))
