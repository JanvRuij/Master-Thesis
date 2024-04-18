import numpy as np
import plotly.graph_objects as go

Sodoku = np.array([
    [1, 2, 3],
    [2, 3, 1],
    [3, 1, 2]])

# x = first dimension
x = [1,2,3,4,5]
# y = second dimension
y = [1,2,3,4,5]
# z = output value
z = [
        [1, 0, 1, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 0, 1],
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 1]
    ]

gO = go.Surface(x=x, y=y, z=z)
fig = go.Figure(data=[gO])

fig.show()
