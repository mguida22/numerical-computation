#!/usr/bin/env python3

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


def euler(fx, fy, fz, initial, h, n):
    x = [None] * n
    y = [None] * n
    z = [None] * n
    t = [None] * n
    x[0], y[0], z[0] = initial
    t[0] = 0

    for i in range(1, n):
        x[i] = x[i-1] + h * fx(x[i-1], y[i-1])
        y[i] = y[i-1] + h * fy(x[i-1], y[i-1], z[i-1])
        z[i] = z[i-1] + h * fz(x[i-1], y[i-1], z[i-1])
        t[i] = i

    return x, y, z, t

def trap(fx, fy, fz, initial, h, n):
    x = [None] * n
    y = [None] * n
    z = [None] * n
    t = [None] * n
    x[0], y[0], z[0] = initial
    t[0] = 0

    x[0] = 0.5 * (x[0] + h * fx(x[0], y[0]))
    y[0] = 0.5 * (y[0] + h * fy(x[0], y[0], z[0]))
    z[0] = 0.5 * (z[0] + h * fz(x[0], y[0], z[0]))
    for i in range(1, n):
        x[i] = x[i-1] + h * fx(x[i-1], y[i-1])
        y[i] = y[i-1] + h * fy(x[i-1], y[i-1], z[i-1])
        z[i] = z[i-1] + h * fz(x[i-1], y[i-1], z[i-1])

        t[i] = i

    x[n-1] = 0.5 * (x[n-1] + h * fx(x[n-1], y[n-1]))
    y[n-1] = 0.5 * (y[n-1] + h * fy(x[n-1], y[n-1], z[n-1]))
    z[n-1] = 0.5 * (z[n-1] + h * fz(x[n-1], y[n-1], z[n-1]))

    return x, y, z, t

res_a_euler = euler(lambda x, y: 16 * (y - x),
                    lambda x, y, z: (45 * x) - y - (x * z),
                    lambda x, y, z: (x * y) - (4 * z),
                    initial = (1, 1, 1),
                    h = 0.01,
                    n = 10000)

res_b_euler = euler(lambda x, y: 16 * (y - x),
                    lambda x, y, z: (45 * x) - y - (x * z),
                    lambda x, y, z: (x * y) - (4 * z),
                    initial = (1.01, 1.01, 1.01),
                    h = 0.01,
                    n = 10000)

res_a_trap = trap(lambda x, y: 16 * (y - x),
                  lambda x, y, z: (45 * x) - y - (x * z),
                  lambda x, y, z: (x * y) - (4 * z),
                  initial = (1, 1, 1),
                  h = 0.01,
                  n = 10000)

res_b_trap = trap(lambda x, y: 16 * (y - x),
                  lambda x, y, z: (45 * x) - y - (x * z),
                  lambda x, y, z: (x * y) - (4 * z),
                  initial = (1.01, 1.01, 1.01),
                  h = 0.01,
                  n = 10000)

# time domain plots
plt.plot(res_a_euler[3], res_a_euler[0], c='red')
plt.plot(res_b_euler[3], res_b_euler[0], c='blue')
plt.show()

plt.plot(res_a_trap[3], res_a_trap[0], c='red')
plt.plot(res_b_trap[3], res_b_trap[0], c='blue')
plt.show()

# state-space plot res_a
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_a_euler[0], res_a_euler[1], res_a_euler[2], c='red')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_a_trap[0], res_a_trap[1], res_a_trap[2], c='red')
plt.show()

# state-space plot res_b
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_b_euler[0], res_b_euler[1], res_b_euler[2], c='blue')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_b_trap[0], res_b_trap[1], res_b_trap[2], c='blue')
plt.show()

# state-space plot both
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_a_euler[0], res_a_euler[1], res_a_euler[2], c='red')
ax.plot(res_b_euler[0], res_b_euler[1], res_b_euler[2], c='blue')
plt.show()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(res_a_trap[0], res_a_trap[1], res_a_trap[2], c='red')
ax.plot(res_b_trap[0], res_b_trap[1], res_b_trap[2], c='blue')
plt.show()
