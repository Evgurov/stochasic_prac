import numpy as np
import matplotlib.pyplot as plt

def fun(x_1, x_2):
    return x_1**3 * np.sin(1/x_1) + 10 * x_1 * x_2**4 * np.cos(1/x_2)

N = 1000

min = 0
x1_min = 0
x2_min = 0
for i in range(N):
    phi = np.random.rand() * 2 * np.pi
    x_1 = np.cos(phi)
    x_2 = np.sin(phi)
    cur_val = fun(x_1, x_2)
    if cur_val < min:
        min = cur_val
        x1_min = x_1
        x2_min = x_2

print("minimum:", min,
      "x1_min:", x1_min,
      "x2_min:", x_2)

x = np.linspace(-1, 1, 100)
y = np.linspace(-1, 1, 100)
X, Y = np.meshgrid(x, y)
Z = fun(X, Y)
Z[X**2 + Y**2 > 1] = None

ax = plt.axes(projection ='3d') 
ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis')

ax.scatter(x1_min, x2_min, min)

plt.show()