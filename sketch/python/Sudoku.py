import numpy as np
from basis import find_xyz, check_symmetry

z = np.matrix([
    [3, 4, 1, 2],
    [2, 1, 3, 4],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
        ])

possible_x = []
possible_y = []
for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        possible_x.append([i, j + 1])
        possible_y.append([i, j + 1])


def Solve(lq):
    has0 = True
    while (has0):
        points = np.empty((0, 2))
        x = possible_x.copy()
        y = possible_y.copy()
        for index in np.ndindex(lq.shape):
            if lq[index] != 0:
                x.remove([index[0], lq[index]])
                y.remove([index[1], lq[index]])
                points = np.vstack(
                        (points,
                         np.array([index[0] - lq[index],
                                   index[1] - lq[index]]))
                        )

        print(check_symmetry(points))
        print(lq)
        print(points)


Solve(z)
