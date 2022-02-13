import numpy as np
import matplotlib.pyplot as plt

def random_walk(grid, i, j):
    rng = np.random.default_rng()
    while grid[i][j] != 2:
        direction = rng.choice([1, 2, 3, 4])
        if direction == 1:
            i -= 1
        elif direction == 2:
            j += 1
        elif direction == 3:
            i += 1
        elif direction == 4:
            j -= 1
    return i, j


f = lambda x, y : x**2 - y**2

h = 0.1

grid_size = int(2 / h + 1)
grid = np.zeros((grid_size, grid_size))

N = 1000

for i in range(grid_size):
    for j in range(grid_size):
        if (-1 + i * h)**2 + (-1 + j * h)**2 <= 1: 
            grid[i][j] = 1

for i in range(grid_size):
    for j in range(grid_size):
        if grid[i][j] == 1:
            if i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:
                grid[i][j] = 2
            elif grid[i-1][j] == 0 or grid[i+1][j] == 0 or grid[i][j-1] == 0 or grid[i][j+1] == 0:
                grid[i][j] = 2


Z = np.zeros((grid_size, grid_size))
sum = 0
i_end, j_end = 0, 0
for i in range(grid_size):
    for j in range(grid_size):
        if grid[i][j] != 0:
            sum = 0
            for n in range(N):
                i_end, j_end = random_walk(grid, i, j)
                sum += f(-1 + j_end * h, -1 + i_end * h)
            Z[i][j] = sum/N
        else:
            Z[i][j] = None


x = np.linspace(-1, 1, grid_size)
y = np.linspace(-1, 1, grid_size)
X, Y = np.meshgrid(x, y)

ax = plt.axes(projection = '3d')
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis')

Z = f(X, Y)
Z[X**2 + Y**2 > 1] = None
ax.plot_wireframe(X, Y, Z)

plt.show()