import numpy as np


X = np.matrix([
    # first ...  # second .. # third . . # fourth .
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0]
    ])

E = np.ones((16, 4))
XT = X.T

transormation = np.dot(X, XT)

print(transormation)

test = np.dot(E.T, X.T)
print(test)
