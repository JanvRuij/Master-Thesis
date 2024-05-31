import numpy as np
from HungarianALG import hungarian_algorithm, ans_calculation
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

z = np.zeros((9, 9))
def LS_Solver(ls):
    size = ls.shape
    arr = np.arange(1, size[1] + 1)
    step = np.tile(arr, (size[1], 1))
    all_steps = np.tile(step, (size[0], 1)).reshape(size[0], size[1], size[1])

    # remove steps based on lq given
    for i in range(size[0]):
        for j in range(size[1]):
            for z in range(1, size[1] + 1):
                if ls[i, j] == z:
                    all_steps[i, j] = np.ones(size[1]) * 1000000
                    all_steps[i, j, z - 1] = z
                    # remove number z from column j items
                    all_steps[i + 1:, j, z - 1] = 1000000
                    # remove number z from row i items
                    all_steps[i, j + 1:, z - 1] = 1000000
                    break

    square = size[0] * size[1]
    shadow = np.ones((square, square)) * 1000000
    for q in range(size[0]):
        for b in range(size[0]):
            for i in range(size[0]):
                shadow[q*size[0] + i, b*size[0] + i] = all_steps[q, b, i]
    
    ans_pos = hungarian_algorithm(shadow.copy())
    ans, ans_mat = ans_calculation(shadow, ans_pos)

    for i in range(square):
        for j in range(square):
            if ans_mat[i, j] != 0:
                column = ((j- size[0]) // size[0]) + 1
                row = ((i- size[0]) // size[0]) + 1

                ls[row, column] = ans_mat[i, j]

	#Show the result
    print(f"Linear Assignment problem result: {ans:.0f}\n{ans_mat}")
    return ls

print(LS_Solver(z))

print('solution')
