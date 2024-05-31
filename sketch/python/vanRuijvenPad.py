import numpy as np
from scipy.optimize import linear_sum_assignment
n = 9
z = np.array([
    [1, 0, 7, 9, 0, 6, 4, 5, 0],
    [0, 2, 5, 3, 4, 0, 0, 0, 8],
    [0, 6, 0, 0, 0, 1, 0, 7, 0],
    [0, 5, 3, 0, 0, 0, 0, 2, 9],
    [6, 1, 0, 0, 0, 9, 8, 0, 0],
    [0, 0, 0, 6, 0, 2, 0, 0, 7],
    [0, 0, 1, 0, 9, 3, 2, 0, 0],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 4, 0, 0, 7, 8, 5, 9, 1],
])
zkjdsfjad = np.array([
    [0, 0, 5, 3, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 2, 0],
    [0, 7, 0, 0, 1, 0, 5, 0, 0],
    [4, 0, 0, 0, 0, 5, 3, 0, 0],
    [0, 1, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 3, 2, 0, 0, 0, 8, 0],
    [0, 6, 0, 5, 0, 0, 0, 0, 9],
    [0, 0, 4, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 9, 7, 0, 0]
])

z = np.array([
    [0, 0, 0, 0, 0, 0, 0, 1, 2],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 7, 3, 0, 2, 6, 0, 0],
    [0, 0, 3, 0, 0, 5, 0, 0, 0],
    [0, 6, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 9, 0, 0, 3, 0, 0],
    [0, 0, 5, 2, 0, 6, 7, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0],
    [9, 1, 0, 0, 0, 0, 0, 0, 0]
])

z = np.array([
    [0, 0, 0, 0, 7, 0, 0, 9, 0],
    [1, 0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 8, 5, 0, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 2],
    [0, 5, 0, 4, 0, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 7],
    [0, 0, 5, 0, 0, 9, 2, 0, 0],
    [0, 0, 6, 0, 0, 0, 0, 0, 4],
    [3, 0, 0, 0, 0, 0, 0, 5, 0]
])


all_steps = np.zeros((n, n, n))

# remove steps based on lq given
for i in range(n):
    for j in range(n):
        for k in range(n):
            if z[i, j] == k + 1:
                all_steps[i, j, k] = 1

ls = np.zeros((n, n, n))

ls = all_steps

def zoekVlakken(ls):
    n, m, z = ls.shape
    vlakken = np.full((n, m, n), True)
    for i in range(n):
        for j in range(n):
            for z in range(n):
                if ls[i, j, z] == 1:
                    vlakken[i, j, :] = False
                    vlakken[i, :, z] = False
                    vlakken[:, j, z] = False
    return vlakken

def DimensionCheck(array):
    n, m = array.shape
    returnarr = np.zeros((n, m))
    for index in np.ndindex(array.shape):
        if array[index] == 1:
            returnarr[index[1], index[1]] = 1
            returnarr[index[0], index[0]] = 1
    return returnarr

def vanRuijvenPad(ls):
    n, m, z = ls.shape
    # loop richtingen
    dir = np.arange(-n + 1, n)
    punt = np.random.randint(0, n, size=3)
    x, y, z = punt
    Row_OS = np.tile(np.eye(n), (m, 1))
    Col_OS = np.tile(np.eye(n), (m, 1))
    OP = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            OP[i, j] = np.sum(np.dot(Row_OS[i * n:i*n + n, :], Col_OS[i * n:i*n + n, :]))
    berijkbaar = zoekVlakken(ls)
    picture = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            for z in range(n):
                if ls[i, j, z] == 1:
                    OP[i, :] -= 1
                    OP[:, j] -= 1
                    picture[i, j] = z + 1
                    row_index = i * n + z
                    col_index = j * n + z
                    Row_OS[row_index, :] = np.zeros(n)
                    Col_OS[col_index, :] = np.zeros(n)

    punt = np.array([0, 0, 0])
    count = 0
    print(OP)
    while np.any(np.sum(ls, axis=2) == 0) and count < n * n + 10:
        best_point = None
        count += 1
        best = -100000000000000000
        for dir_x in dir:
            for dir_y in dir:
                for dir_z in dir:
                    nieuw_punt = punt + np.array([dir_x, dir_y, dir_z])
                    x, y, z = nieuw_punt
                    if np.all((nieuw_punt >= 0) & (nieuw_punt < m)):
                        if berijkbaar[x, y, z]:
                            stupid = False
                            Row_OS_test = Row_OS.copy()
                            Col_OS_test = Col_OS.copy()
                            OP_test = OP.copy()
                            OP_test[x, :] -= 1
                            OP_test[:, y] -= 1
                            OP_test[OP_test < 1] = 1
                            row_index = y * n + z
                            col_index = x * n + z
                            Row_OS_test[row_index, :] = np.zeros(n)
                            Col_OS_test[col_index, :] = np.zeros(n)
                            for indeces in np.ndindex((n, m)):
                                i, j = indeces
                                row_index = i * n
                                col_index = j * n
                                if np.sum(np.dot(Row_OS_test[row_index: row_index + n, :], Col_OS_test[col_index:col_index + n])) < 1 and np.sum(ls[i, j, :]) == 0:
                                    stupid = True
                            if not stupid:
                                best_point = x, y, z

        if best_point is not None:
            punt = best_point 
            x, y, z = punt
            row_index = y * n + z
            col_index = x * n + z
            Row_OS[row_index, :] = np.zeros(n)
            Col_OS[col_index, :] = np.zeros(n)
            berijkbaar[:, y, z] = False
            berijkbaar[x, :, z] = False
            berijkbaar[x, y, :] = False
            ls[x, y, z] = 1
            picture[x, y] = z + 1
            print(picture)
        else:
            print("no point found!!")

    return ls

ls = vanRuijvenPad(ls)
picture = np.zeros((n, n))
for i in range(n):
    for j in range(n):
        for z in range(n):
            if ls[i, j, z] == 1:
                picture[i, j] = z + 1
print(picture)