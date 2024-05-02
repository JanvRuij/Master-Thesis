import numpy as np


def check_symmetry(points):
    symmetric = True
    for point in points:
        reflection = [point[0] - point[1], - point[1]]
        # Check if the reflection exists in the set of points
        if not any(np.all(reflection == p) for p in points):
            symmetric = False
            break
    return symmetric


def find_xyz(arr, possible_x, possible_y):
    result = []
    for x, z in possible_x:
        for y, z_ in possible_y:
            if x - z == arr[0] and y - z_ == arr[1]:
                result.append((x, y, z))
    return result
