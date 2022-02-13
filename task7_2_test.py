import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt

def Rosenbrock(x_1, x_2):
    return (x_1 - 1)**2 + 100 * (x_2 - x_1**2)**2


T_0 = 20
sigma = 0.3
k = 0.95
eps = 0.00001

ax = plt.axes(projection = '3d')

x_prev = 0
y_prev = 0
T = T_0
while T > eps:
    x_next = sps.norm.rvs(loc = x_prev, scale = sigma * T, size = 1)
    y_next = sps.norm.rvs(loc = y_prev, scale = sigma * T, size = 1)
    delta_F = Rosenbrock(x_next, y_next) - Rosenbrock(x_prev, y_prev)
    if delta_F <= 0:
        x_prev = x_next
        y_prev = y_next
        ax.plot(x_prev, y_prev, 'o', color = 'b')
    else:
        if np.random.rand() < np.exp(-delta_F / T):
            x_prev = x_next
            y_prev = y_next
            ax.plot(x_prev, y_prev, 'o', color = 'b')
    T = k * T


print("Minimum point:", x_prev, y_prev, "Minimum value:", Rosenbrock(x_prev, y_prev))

x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)
Z = Rosenbrock(X, Y)

ax.plot_surface(X, Y, Z, rstride = 1, cstride = 1, cmap = 'viridis')

ax.scatter(x_prev, y_prev, Rosenbrock(x_prev, y_prev), color = 'r')

plt.show()