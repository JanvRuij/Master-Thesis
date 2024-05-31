import numpy as np

# Initialize the three possible row vectors
row_vectors = np.array([[1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])

# Initialize the 9x3 matrix
matrix = np.zeros((9, 3), dtype=int)

# Function to check the dot product condition for a row
def is_valid_row(row, matrix, row_index, n, m):
    all_div = np.ones(m) - row
    all_col = np.ones(m) - row
    division = row_index // m
    column = row_index % m
    if row_index == 4:
        print('debug')
        print(row)
    # first dimension check
    for i in range(m):
        row_nr = division * m + i
        all_div = all_div - matrix[row_nr]
        if row_nr != row_index and np.dot(row, matrix[row_nr]) != 0:
            return False

    for i in range(m):
            row_nr = division * m + i
            if row_nr > row_index and np.dot(all_div, matrix[row_nr]) != 0:
                return False

    # second dimensioncheck
    for i in range(m):
        row_nr = column + i * m
        all_col = all_col - matrix[row_nr]
        if row_nr != row_index and np.dot(row, matrix[row_nr]) != 0:
            return False

    for col in range(column + 1, m): 
        for div in range(m):
            row_nr = col + div * m
            if row_nr != row_index and np.sum(all_col) - np.dot(all_col, matrix[row_nr]) == 0:
                return False

    return True

# Generate the matrix row by row
for row_index in range(9):
    added = False
    n, m = matrix.shape
    for row in row_vectors:
        if is_valid_row(row, matrix, row_index, n, m):
            matrix[row_index] = row
            added = True
            print(matrix)
            break

    if not added:
        raise ValueError(f'No valid row could be found for row {row_index + 1}')

# Display the resulting matrix
print(matrix)
