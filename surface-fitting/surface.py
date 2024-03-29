#!/usr/bin/env python3

from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.pyplot as plt
import numpy as np


top = np.array([
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
])

bottom = np.array([
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
])

np.sort(top, axis=0)
np.sort(bottom, axis=0)

# use midpoints to calculate more points for our surface
x_top = []
y_top = []
z_top = []
x_bottom = []
y_bottom = []
z_bottom = []
for i in range(0, len(top)):
    # ax.scatter(top[i][0], top[i][1], top[i][2], c='red')
    x_top.append(top[i][0])
    y_top.append(top[i][1])
    z_top.append(top[i][2])

    if (i+1 < len(top)):
        x_top.append((top[i][0] + top[i+1][0]) / 2)
        y_top.append((top[i][1] + top[i+1][1]) / 2)
        z_top.append((top[i][2] + top[i+1][2]) / 2)

    if (i+2 < len(top)):
        x_top.append((top[i][0] + top[i+2][0]) / 2)
        y_top.append((top[i][1] + top[i+2][1]) / 2)
        z_top.append((top[i][2] + top[i+2][2]) / 2)

for i in range(0, len(bottom)):
    # ax.scatter(bottom[i][0], bottom[i][1], bottom[i][2], c='blue')
    x_bottom.append(bottom[i][0])
    y_bottom.append(bottom[i][1])
    z_bottom.append(bottom[i][2])

    if (i+1 < len(bottom)):
        x_bottom.append((bottom[i][0] + bottom[i+1][0]) / 2)
        y_bottom.append((bottom[i][1] + bottom[i+1][1]) / 2)
        z_bottom.append((bottom[i][2] + bottom[i+1][2]) / 2)

    if (i+2 < len(bottom)):
        x_bottom.append((bottom[i][0] + bottom[i+2][0]) / 2)
        y_bottom.append((bottom[i][1] + bottom[i+2][1]) / 2)
        z_bottom.append((bottom[i][2] + bottom[i+2][2]) / 2)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_trisurf(x_top, y_top, z_top, cmap=cm.coolwarm, linewidth=0.2)
ax.plot_trisurf(x_bottom, y_bottom, z_bottom, cmap=cm.coolwarm, linewidth=0.2)

plt.show()
