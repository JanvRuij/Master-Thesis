import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


# minimize sum_i sum_a1i * xi / pi such that:
# A * x >= b
A = np.matrix([
    [2, 0, 1],
    [0, 1, 1],
    [1, 3, 0],
    ])

n_rows, n_columns = A.shape
b = np.array([1, 5, 3])
prio = np.array([1, 1, 1])

# going to draw the corresponding polytope
size = 5
# start creating the points that need to be colored
print("Started")
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
points = np.empty((0, 3))
for row in range(n_rows):
    xx, yy = np.meshgrid(range(size), range(size))
    plane = None
    if A[row, 0] > 0:
        plane = (b[row] - A[row, 1] * xx - A[row, 2] * yy) / A[row, 0]
    elif A[row, 1] > 0:
        plane = (b[row] - A[row, 0] * xx - A[row, 2] * yy) / A[row, 1]
    elif A[row, 2] > 0:
        plane = (b[row] - A[row, 0] * xx - A[row, 1] * yy) / A[row, 2]

    # Plot points
    ax.plot_surface(xx, yy, plane, alpha=0.2)

# Adjust layout
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
ax.set_xlim([0, 5])
ax.set_ylim([0, 5])
ax.set_zlim([0, 5])
plt.tight_layout()

# Show plot
plt.show()
