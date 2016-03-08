#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np
from numpy import zeros

x = [1., 2., 3., 4., 5., 6., 7.]
y = [1., 3., 2., 1., 2., 4., 5.]
n = len(x)

a = zeros(n)
dx = zeros(n)
dy = zeros(n)
for i in range(0, n-1):
    dx[i] = x[i+1] - x[i]
    dy[i] = y[i+1] - y[i]

# Somethings broken here
# Solve (3.24) for c1..cn
A = zeros((n, n))
r = zeros((n, 1))

A[0][0] = 1
A[n-1][n-1] = 1
r[0] = 0
r[n-1] = 0

for i in range(1, n-1):
	A[i][i-1] = dx[i]
	A[i][i] = 2 * (dx[i] + dx[i+1])
	A[i][i+1] = dx[i+1]
	r[i] = 3 * ((dy[i+1] / dx[i+1]) - (dy[i] / dx[i]))
	if np.isnan(r[i]):
		r[i] = 0

print(A)
print(r)

c = np.linalg.solve(A, r)
print(c)

d = zeros(n)
b = zeros(n)
for i in range(0, n-1):
    d[i] = (c[i+1] - c[i]) / (3 * dx[i])
    b[i] = (dy[i] / dx[i]) - ((dx[i] / 3) * (2 * c[i] + c[i+1]))

for i in range(0, n-1):
    print('S{i}(x) = {a} + {b}(x - {x}) + {c}(x - {x})^2 + {d}(x - {x})^3'.format(i=i, a=y[i], b=b[i], c=c[i][0], d=d[i], x=x[i]))


plt.plot(x, y)
plt.title('Cubic Splines',fontsize=10)
plt.show()



