#!/usr/bin/env python3

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

top = [
    (33.44, 87.93, 105.88),
    (8.81, 84.07, 103.11),
    (15.62, 34.83, 105.98),
    (40.16, 38.71, 108.13),
    (61.45, 67.07, 108.12),
    (58.81, 91.44, 107.72),
    (36.97, 63.29, 107.14),
    (64.71, 42.38, 109.07),
    (89.11, 46.49, 109.93),
    (67.24, 18.32, 109.99),
    (65.90, 31.93, 109.51),
    (76.55, 44.51, 109.91)
]

bottom = [
    (15.59, 35.07, 12.88),
    (38.57, 37.17, 13.33),
    (61.10, 67.15, 17.31),
    (58.97, 92.05, 19.09),
    (36.98, 63.24, 16.51),
    (64.45, 42.66, 20.01),
    (89.18, 46.85, 27.71),
    (66.87, 18.48, 14.24),
    (65.90, 31.93, 21.0),
    (76.55, 44.51, 22.0),
]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

for i in range(0, len(top)):
    ax.scatter(top[i][0], top[i][1], top[i][2], c='red')

for i in range(0, len(bottom)):
    ax.scatter(bottom[i][0], bottom[i][1], bottom[i][2], c='blue')

plt.show()
