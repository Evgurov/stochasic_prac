import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

def Wiener(N):
    t = np.linspace(0, 1, 2**(N - 1) + 1)
    W = np.array([0, sps.norm.rvs(0,1)])
    for k in range(1,N):
        m = (W[:-1] + W[1:])/2
        s = np.sqrt(1/(2**(k + 1)))
        new_W = np.zeros(2**k + 1)
        new_W[::2] = W
        new_W[1::2] = sps.norm.rvs(m, s, m.shape)
        W = new_W
    return t, W

t, W = Wiener(15)
sns.scatterplot(t, W, s = 4)
plt.ylabel(r'$W_t$')
plt.xlabel(r'$t$')

plt.show()