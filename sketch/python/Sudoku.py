import numpy as np
from scipy.optimize import linear_sum_assignment

z = np.zeros((9, 9))



def LS_Solver(ls):
    size = ls.shape
    unsolved = np.any(ls == 0)
    arr = np.arange(1, size[1] + 1)
    step = np.tile(arr, (size[1], 1))
    all_steps = np.tile(step, (size[0], 1)).reshape(size[0], size[1], size[1])

    # remove steps based on lq given
    for i in range(size[0]):
        for j in range(size[1]):
            for z in range(1, size[1] + 1):
                if ls[i, j] == z:
                    all_steps[i, j] = np.zeros(size[1])
                    all_steps[i, j, z - 1] = z
                    # remove number z from column j items
                    all_steps[i + 1:, j, z - 1] = 0 
                    # remove number z from row i items
                    all_steps[i, j + 1:, z - 1] = 0
                    break

    count = 0
    while (unsolved and count < 1):
        for i in range(size[0]):
            for j in range(size[1]):
                for z in range(1, size[1] + 1):
                    if np.all(ls[i] != z) and np.all(ls.T[j] != z) and ls[i, j] == 0:
                        smart_step = True
                        test_step = np.copy(all_steps)
                        # remove number z from column j items
                        test_step[i + 1:, j, z - 1] = 0 
                        # remove number z from row i items
                        test_step[i, j + 1:, z - 1] = 0
                        square = size[0] * size[1]
                        shadow = np.zeros((square, square))
                        shadowT = np.zeros((square, square))
                        n = size[0]

                        for q in range(size[0]):
                            for b in range(size[0]):
                                shadow[q*n + b, b*n:b*n + n] = -test_step[q, b]
                                shadowT[b*n:b*n + n,q*n + b] = -test_step[b, q]

                        row_indices, col_indices = linear_sum_assignment(shadow)
                        for row, col in zip(row_indices, col_indices):
                            if shadow[row, col] == 0:
                                smart_step = False

                        row_indices, col_indices = linear_sum_assignment(shadowT)
                        for row, col in zip(row_indices, col_indices):
                            if shadowT[row, col] == 0:
                                smart_step = False

                        if smart_step:
                            all_steps = test_step
                            ls[i, j] = z
                            break
                    
                    
        count += 1
        unsolved = np.any(ls == 0)
    return ls

print(LS_Solver(z))

print('solution')
