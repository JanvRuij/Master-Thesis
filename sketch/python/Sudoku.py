import numpy as np
import plotly.graph_objects as go


# x = first dimension
x = np.arange(0, 9)
xr = np.arange(1, 10)
# y = second dimension
y = np.arange(0, 9)
yr = np.arange(1, 10)
# z = output value of shadow 4th dimension
z = np.matrix([
    [0, 0, 0, 8, 0, 0, 0, 0, 9],
    [0, 1, 9, 0, 0, 5, 8, 3, 0],
    [0, 4, 3, 0, 1, 0, 0, 0, 7],
    [4, 0, 0, 1, 5, 0, 0, 0, 3],
    [0, 0, 2, 7, 0, 4, 0, 1, 0],
    [0, 8, 0, 0, 9, 0, 6, 0, 0],
    [0, 7, 0, 0, 0, 6, 3, 0, 0],
    [0, 3, 0, 0, 7, 0, 0, 8, 0],
    [9, 0, 4, 5, 0, 0, 0, 0, 1],
])
# f = fourth dimension
f = np.arange(0, 9)

zsol = [[[np.arange(1, 10)] for _ in range(9)] for _ in range(9)]

gO = go.Surface(x=xr, y=yr, z=z)
fig = go.Figure(data=[gO])

# fig.show()

# Lets create polynomial solver!
for q in f:
    for q in f:
        for i in x:
            for j in y:
                if i > 0:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i - 1, j]))
                if j > 0:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i, j - 1]))
                if i + j > 1:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i - 1, j - 1]))
                if i < 8:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i + 1, j]))
                if j < 8:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i, j + 1]))
                if i < 8 and j < 8:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i + 1, j + 1]))
                if i > 0 and j < 8:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i - 1, j + 1]))
                if i < 8 and j > 0:
                    zsol[i][j] = np.delete(zsol[i][j], np.where(zsol[i][j] == z[i + 1, j - 1]))

print(zsol)
