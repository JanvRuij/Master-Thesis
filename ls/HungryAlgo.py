import numpy as np
from scipy.optimize import linear_sum_assignment


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

z = np.zeros((3, 3))
def hungry(matrix):
    n, m = matrix.shape
    sol = matrix
    arr = np.arange(1, n + 1)
    step = np.tile(arr, (n, 1))
    all_steps = np.tile(step, (n, 1)).reshape(n, n, n)
    for i in range(n):
        for j in range(n):
            for z in range(1, n + 1):
                if matrix[i, j] == z:
                    all_steps[i, j] = np.ones(n) * 1000000
                    all_steps[i, j, z - 1] = z
                    # remove number z from column j items
                    all_steps[i + 1:, j, z - 1] = 1000000
                    # remove number z from row i items
                    all_steps[i, j + 1:, z - 1] = 1000000
                    break
    # substract lowest elements from each row-col-tube
    for i in range(n):
        for j in range(m):
            min = np.min(all_steps[i, j, :])
            all_steps[i, j, :] = all_steps[i, j, :] - min
    
    trans = np.transpose(all_steps, (0, 2, 1))
    if check_0s(all_steps, n, m) and check_0s(all_steps.T, n, m) and check_0s(trans, n, m):
        pass
        # have enough 0's, now we can start assigning 
    else:
        for i in range(n):
            for j in range(m):
                min = np.min(all_steps.T[i, j, :])
                all_steps.T[i, j, :] = all_steps.T[i, j, :] - min

    trans = np.transpose(all_steps, (2, 1, 0))
    print(all_steps)
    if check_0s(all_steps, n, m) and check_0s(all_steps.T, n, m) and check_0s(trans, n, m):
       # have enough 0's can start assignment 
       for i in range(n):
           for j in range(m):
                for z in range(n):
                    if all_steps[i, j, z] == 0:
                        real_num = z + 1
                        if not np.any(sol[:, j] == real_num) and not np.any(sol[i, :] == real_num):
                            sol[i, j] = real_num
                            break
    
    return sol



def check_0s(matrix, n, m):
    for i in range(n):
        for j in range(m):
            row0s = np.count_nonzero(matrix[i, j] == 0)
            col0s = np.count_nonzero(matrix[i, :, j] == 0)
            if col0s < 1 or row0s < 1:
                return False
    return True

step1 = hungry(z)
print(hungry(step1))