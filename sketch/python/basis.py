import numpy as np


def check_symmetry(points):
    symmetric = True
    non_symmetric_points = []
    for point in points:
        reflection = symmetrizizer(point)
        # Check if the reflection exists in the set of points
        if not any(np.all(reflection == p) for p in points):
            symmetric = False
            non_symmetric_points.append(reflection)
    return symmetric, non_symmetric_points


def symmetrizizer(point):
    return [point[0] - point[1], - point[1]]


def find_xyz(non_symmetric_points, possible_x, possible_y):
    for arr in non_symmetric_points:
        for x, z in possible_x:
            for y, z_ in possible_y:
                if z_ == z and x - z == arr[0] and y - z_ == arr[1]:
                    return [x, y, z]


def counter(list, index):
    count = 0
    for i in list:
        if i[0] == index:
            count += 1
    return count
