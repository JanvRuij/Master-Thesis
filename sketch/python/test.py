import numpy as np
from scipy.optimize import linear_sum_assignment

# Define the cost matrix
cost_matrix = np.array([
    [0, 0, 3, 4, 5, 6, 7, 8, 9],
    [1, 0, 3, 4, 5, 6, 7, 8, 9],
    [0, 0, 0, 4, 5, 6, 7, 8, 9],
    [0, 0, 3, 0, 5, 6, 7, 8, 9],
    [0, 0, 0, 0, 0, 6, 7, 8, 9],
    [0, 0, 0, 0, 5, 0, 7, 8, 9],
    [0, 0, 0, 0, 0, 0, 0, 8, 9],
    [0, 0, 0, 0, 0, 0, 7, 0, 9],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
])
cost_matrix = - cost_matrix
# Find the optimal assignment using linear_sum_assignment
row_indices, col_indices = linear_sum_assignment(cost_matrix)

# Print the optimal assignment
print("Optimal Assignment:")
for row, col in zip(row_indices, col_indices):
    print(f"Task {row} is assigned to Resource {col} (Cost: {cost_matrix[row, col]})")
