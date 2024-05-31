import numpy as np
import pulp

# Define the set of indices (assuming n x n matrix)
n = 5
indices = range(n ** 2)
c = np.zeros((n, n))


arr = np.arange(1, n + 1)
step = np.tile(arr, (n, 1))
all_steps = np.tile(step, (n, 1)).reshape(n, n, n)
for i in range(n):
    for j in range(n):
        for z in range(1, n + 1):
            if c[i, j] == z:
                all_steps[i, j] = np.ones(n) * 1000000
                all_steps[i, j, z - 1] = z
                # remove number z from column j items
                all_steps[i + 1:, j, z - 1] = 1000000
                # remove number z from row i items
                all_steps[i, j + 1:, z - 1] = 1000000
                break

square = n ** 2
shadow = np.ones((square, square)) * 1000000
for q in range(n):
    for b in range(n):
        for i in range(n):
            shadow[q*n + i, b*n + i] = all_steps[q, b, i]

print(shadow)
# Create the ILP problem
prob = pulp.LpProblem("ILP Problem", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in indices for j in indices], cat='Binary')

# Define the objective function
prob += pulp.lpSum(x[(i, j)] * shadow[i, j] for i in indices for j in indices)

# Constraints: sum_i x_ij = 1 for all j
for j in indices:
    prob += pulp.lpSum(x[(i, j)] for i in indices) == 1

# Constraints: sum_j x_ij = 1 for all i
for i in indices:
    prob += pulp.lpSum(x[(i, j)] for j in indices) == 1

# Define the dimensions of the matrix
matrix_size = square
submatrix_size = n
subsets = []
for i in range(0, square, submatrix_size):
    for j in range(submatrix_size):
        s = []
        for b in range(submatrix_size):
            s.append((i + b,  j*submatrix_size + b))
        subsets.append(s)
print(subsets)
for subset in subsets:
    prob += pulp.lpSum(x[i] for i in subset) == 1
# Solve the ILP problem
prob.solve()

# Print the solution
print("Solution:")
sol = np.zeros((square, square))
count = 0
for i in range(square):
    for j in range(square):
        sol[i, j] = int(prob.variables()[i * matrix_size + j].value())

sudoku = np.zeros((n, n))
for i in range(square):
    for j in range(square):
        if sol[i, j] != 0:
            column = ((j- n) // n) + 1
            row = ((i- n) // n) + 1
            sudoku[column, row] = shadow[i, j]

print(sudoku)
print("Objective =", pulp.value(prob.objective))