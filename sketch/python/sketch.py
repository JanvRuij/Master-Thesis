import numpy as np
import matploblib

A = np.matrix([
    [2, 0, 1],
    [0, 1, 1],
    [1, 3, 0],
    [0, 1, 0],
    [0, 1, 0]
    ])
b = np.array([1, 5, 3, 11, 8])
prio = np.array([1, 1, 1])

# minimize sum(a1)x1 / p1 such that:
# A * x >= b

