# most important part
import numpy as np

# latin square
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

z_start = z.copy()
# need some memory
n, m = z.shape
numbers = np.arange(1, n + 1)
for i in range(n):
    for j in range(n):
        for num in numbers:
            if num not in z[i] and z[i, j] == 0:
                z[i, j] = num
                break


def find_duplicates_in_column(column):
    unique_elements, counts = np.unique(column, return_counts=True)
    duplicates = unique_elements[counts > 1]
    return duplicates

def location_counter(array, numbers):
    n, _ = array.shape
    locations = np.zeros((n, n))
    location_counter = np.zeros((n, n))
    for num in numbers:
        for i in range(n):
            for j in range(n):
                if array[i, j] == num:
                    locations[num - 1, i] = j
    for i in range(n):
        for j in range(n):
            location_counter[i, int(locations[i, j])] += 1
    return location_counter

def potential_entropy(array):
    for c1 in range(n):
        dubs = find_duplicates_in_column(array[:, c1])
        for num in dubs:
            rows = np.where(array[:, c1] == num)[0]
            for row in rows:
                if z_start[row, c1] != 0:
                    for c2 in range(n):
                        entropy = 0
                        if c1 != c2:
                            s1 = len(np.unique(array[:, c1])) 
                            s2 = len(np.unique(array[:, c2])) 
                            array_test = array.copy()
                            if z_start[row, c2] == 0:
                                temp = array_test[row, c1]
                                array_test[row, c1] = array_test[row, c2]
                                array_test[row, c2] = temp
                                s1c = len(np.unique(array_test[:, c1]))
                                s2c = len(np.unique(array_test[:, c2]))
                                if (s1c - s1) / s1 + (s2c - s2) / s2 > 0:
                                    entropy += 1
                                    break
                    if entropy == 0:
                        return False
    return True

def swap(n1, c1, c2, array):
    rows = np.where(array[:, c1] == n1)[0]
    array_test = array.copy()
    s1 = len(np.unique(array[:, c1])) 
    s2 = len(np.unique(array[:, c2])) 
    for row in rows:
        if z_start[row, c1] == 0 and z_start[row, c2] == 0:
            temp = array_test[row, c1]
            array_test[row, c1] = array_test[row, c2]
            array_test[row, c2] = temp
            s1c = len(np.unique(array_test[:, c1]))
            s2c = len(np.unique(array_test[:, c2]))
            if (s1c - s1) / s1 + (s2c - s2) / s2 > 0:
                if potential_entropy(array_test):
                    array = array_test
                    return array, True
                
    return array, False
    
for count in range(n*n*n):
    locations_count = location_counter(z, numbers)
    print(locations_count)
    excess = np.argsort(locations_count.flatten())[::-1]
    rand = np.random.uniform(0, 1)
    for i in excess:
        finished = False
        index = np.unravel_index(i, locations_count.shape)
        n1, column1 = index
        for j in excess:
            index_0 = np.unravel_index(j, locations_count.shape)
            n2, column2 = index_0
            if column1 != column2 and rand > 0.5:
                z, finished = swap(n1 + 1, column1, column2, z) 
                print(z)

print(locations_count)
print(z)