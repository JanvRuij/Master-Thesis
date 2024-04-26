z = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [2, 3, 0, 5, 6, 7, 8, 9, 1],
    [3, 4, 0, 6, 7, 8, 9, 1, 2],
    [4, 5, 0, 7, 8, 9, 1, 2, 3],
    [0, 6, 7, 8, 9, 1, 2, 3, 4],
    [6, 7, 8, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 1, 2, 3, 4, 5, 6],
    [8, 9, 1, 2, 3, 4, 5, 6, 7],
    [9, 1, 2, 3, 4, 5, 6, 7, 8]
]
contains_0 = True

while(contains_0):
    zT = list(zip(*z))
    x_z_combos = []
    y_z_combos = []
    for i in range(9):
        for j in range(1, 10):
            x_z_combos.append([i, j])
            y_z_combos.append([i, j])

    for i in range(9):
        for j in z[i]:
            if j != 0:
                x_z_combos.remove([i, j])

    for i in range(9):
        for j in zT[i]:
            if j != 0:
                y_z_combos.remove([i, j])

    for p in x_z_combos:
        for q in y_z_combos:
            if p[1] == q[1]:
                z[p[0]][q[0]] = q[1]

    has0 = False
    for i in range(9):
        for j in range(9):
            if z[i][j] == 0:
                has0 = True
    contains_0 = has0

print(z)
print(z)
