import numpy as np
import scipy.stats as sps
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()

def Orn_Uhl(a,s,th,N):
    t = np.linspace(0, 1, 2**(N - 1) + 1)
    ou = np.array([sps.norm.rvs(a, s**2), sps.norm.rvs(0, s**2 * (1 - np.e**(-2 * th)))])
    for k in range(1, N):
        dt = 1 / 2**(k - 1)
        sum = (ou[:-1] + ou[1:])
        e  = np.ones(2**(k - 1)) * np.e**(-th * dt)
        e2  = np.ones(2**(k - 1)) * np.e**(-th * dt / 2)
        mean = sum * e2 / (1 + e)
        sigma2 = s**2 * (1 - e) / (1 + e)
        new_ou = np.zeros(2**k + 1)
        new_ou[::2] = ou
        new_ou[1::2] = sps.norm.rvs(mean, sigma2, e.shape)
        ou = new_ou
    return t, ou

t,ou = Orn_Uhl(0, 1, 50, 16)
sns.scatterplot(t, ou, s = 3)
plt.ylabel(r'$X_t$')
plt.xlabel(r'$t$')

plt.show()