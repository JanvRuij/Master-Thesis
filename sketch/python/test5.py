import numpy as np

z = np.array([
    [2, 1],
    [6, 8],
    [5, 6],
    [4, 5],
    [9, 4],
    [1, 7],
    [7, 3],
    [3, 8],
    [9, 2]
])
while np.sum(z[:, 1]) != 45:
    for i in range(1, 10):
        if np.count_nonzero(z[:, 0] == i) == 2:
            for j in range(z.shape[0]):
                if z[j, 0] == i:
                    temp = z[j, 1]
                    z[j, 1] = z[j, 0]
                    z[j, 0] = temp
                    break
        print(z)

        
