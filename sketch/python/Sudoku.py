import numpy as np
import matplotlib.pyplot as plt


z = np.zeros((9, 9))


def Solve(lq):
    size = lq.shape
    possible_x = []
    possible_y = []
    for i in range(size[0]):
        for j in range(size[1]):
            possible_x.append([i, j + 1])
            possible_y.append([i, j + 1])

    lq, solved = Sodoku_Solver(possible_x, possible_y, lq)
    if solved:
        return lq
    else:
        return "not solvable"


def Sodoku_Solver(possible_x, possible_y, lq):
    size = lq.shape
    x = possible_x.copy()
    y = possible_y.copy()
    solved = False
    step_taken = False
    for i in range(size[0]):
        for j in range(size[1]):
            if lq[i, j] != 0:
                x.remove([i, lq[i, j]])
                y.remove([j, lq[i, j]])
    for i in x:
        for j in y:
            if i[1] == j[1] and lq[i[0], j[0]] == 0:
                lq[i[0], j[0]] = j[1]
                step_taken = True
                lq, solved = Sodoku_Solver(possible_x, possible_y, lq.copy())
                if solved:
                    return lq, solved

    if not step_taken:
        return lq, False

    solved = np.any(lq != 0)
    return lq, solved


print(Solve(z))
