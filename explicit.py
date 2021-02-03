import numpy as np
from matplotlib import pyplot as plt

dr: float = 5.0e-3
dx = 0.01
xlast = 1
rlast = 0.1
r = range(int(rlast / dr) + 1)
r = [i * dr for i in r]
x = range(int(xlast / dx) + 1)
x = [dx * i for i in x]
Ro = 1
U = 2.5
Cp = 4200
K = 10
Lambda = dx * K / Ro / U / Cp / dr
t = np.zeros((len(x), len(r)))
t[0, :] = 800
t[:, -1] = 20
for i in range(int(xlast / dx) + 1)[:-1]:
    for k in range(int(rlast / dr) + 1)[1:-1]:
        t[i + 1, k] = Lambda * ((t[i, k + 1] - t[i, k]) / r[k] + (t[i, k + 1] - 2 * t[i, k] + t[i, k - 1]) / dr) + t[
            i, k]
        t[i + 1, 0] = t[i + 1, 1]
t[-1, 0] = t[-1, 1]
plt.figure(1)
plt.plot(x, t)
plt.figure(2)
x, r = np.meshgrid(x, r)
plt.contourf(x, r, np.transpose(t))
plt.show()