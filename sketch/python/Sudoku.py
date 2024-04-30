import numpy as np
from basis import find_xyz, find_symmetric_point, check_symmetry

z = np.matrix([
    [3, 4, 1, 2],
    [2, 1, 3, 4],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
        ])


def Solve(lq):
    points = np.empty((0, 2))
    for index in np.ndindex(lq.shape):
        if lq[index] != 0:
            points = np.vstack(
                    (points,
                     np.array([index[0] - lq[index], index[1] - lq[index]]))
                    )

    print(check_symmetry(points))
    points = np.vstack((points, find_symmetric_point(points)))
    print(check_symmetry(points))

    points = np.vstack((points, find_symmetric_point(points)))
    print(check_symmetry(points))
    print(lq)
    print(points)


Solve(z)
