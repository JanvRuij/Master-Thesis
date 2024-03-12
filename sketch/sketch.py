import numpy as np


# min f(x) such that x is in a cone and rank(x) = §1
# Create adjecency matrix
A = np.random.randint(2, (20, 20))
X = np.zeros((20, 20))
x = np.random.randint(2, size=20)
x = x * 2 - 1
print(x)
