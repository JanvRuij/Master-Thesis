import numpy as np
import matplotlib


# minimize sum_i sum_a1i * xi / pi such that:
# A * x >= b
A = np.matrix([
    [2, 0, 1],
    [0, 1, 1],
    [1, 3, 0],
    [0, 1, 0],
    [0, 1, 0]
    ])
n_rows, n_columns = A.shape
b = np.array([1, 5, 3, 11, 8])
prio = np.array([1, 1, 1])

# going to draw the corresponding polytope
size = 100
x1 = np.linspace(0, 20, size)
x2 = np.linspace(0, 20, size)
x3 = np.linspace(0, 20, size)

for row in range(0, 1):
    line = np.zeros((size * size, 3))
    pivot_v = 0
    pivot_idx = 0
    for idx, x in np.ndenumerate(A[row]):
        if x > 0:
            pivot_idx = idx[0]
            pivot_v = x
            break
    counter = 0
    for idx2, x2_v in np.ndenumerate(x3):
        for idx3, x3_v in np.ndenumerate(x3):
            value = (b[row] - A[row, 1] * x2_v - A[row, 2] * x3_v) / pivot_v
            line[counter, 0] = value
            line[counter, 1] = x2_v
            line[counter, 2] = x3_v
            counter += 1

    print(line)


