#!/usr/bin/env python3

from numpy import zeros

x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 2, 1, 2, 4, 5]
n = len(x)

a = zeros(n)
dx = zeros(n)
dy = zeros(n)
for i in range(0, n-2):
    dx[i] = x[i+1] - x[i]
    dy[i] = y[i+1] - y[i]

# Somethings broken here
# Solve (3.24) for c1..cn
# A = zeros((n, n))
# r = zeros((n, 1))

# for i in range(1, n-2):
# 	r[i] = 3 * ((dy[i] / dx[i]) - (dy[i-1] / dx[i-1]))
# 	A[i][i-1] = dx[i-1]
# 	A[i][i] = 2 * (dx[i-1] + dx[i])
# 	A[i][i+1] = dx[i]

# A[1][1] = 1
# A[n-1][n-1] = 1

# c = zeros((n, 3))
# for i in range(0, n-1):
# 	c[i][2] = (A / r)

# for i in range(0, n-2):
# 	c[i][3] = (c[i+1][2] - c[i][2]) / (3 * dx[i])
# 	c[i][1] = (dy[i] / dx[i]) - dx[i] * (2 * c[i][2] + c[i+1][2] / 3)

# print(c)

for i in range(0, n-2):
    d[i] = (c[i+1] - c[i]) / (3 * dx[i])
    b[i] = (dy[i] / dx[i]) - ((dx[i] / 3) * (2 * c[i] + c[i+1]))

for i in range(0, len(x)-1):
    print('S{i}(x) = {a} + {b}(x - {x}) + {c}(x - {x})^2 + {d}(x - {x})^3').format(i, a=y[i], b=b[i], c=c[i], d=d[i], x=x[i])
