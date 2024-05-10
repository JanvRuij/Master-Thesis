import numpy as np
from scipy.optimize import linear_sum_assignment

z = np.zeros((50, 50))



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
    while (unsolved and count < 1000):
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

                        for q in range(size[0]):
                            cost_matrix_col = - test_step[q, :]
                            cost_matrix_row = - test_step[:, q]
                            row_indices_col, col_indices_col = linear_sum_assignment(cost_matrix_col)
                            row_indices_row, col_indices_row= linear_sum_assignment(cost_matrix_row)
                            for row, col in zip(row_indices_row, col_indices_row):
                                if cost_matrix_row[row, col] == 0:
                                    smart_step = False
                            for row, col in zip(row_indices_col, col_indices_col):
                                if cost_matrix_col[row, col] == 0:
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
