import numpy as np
from matplotlib import pyplot as plt 
dr = 5.0e-3
dx = 0.01
xlast = 1
rlast = 0.1
r = range(int(rlast/dr)+1)
r = [i*dr for i in r]
x = range(int(xlast/dx)+1)
x = [dx*i for i in x]
Ro = 1
U = 2.5
Cp = 4200
K = 10
Lambda = dx*K/Ro/U/Cp/dr
t = np.zeros((len(x),len(r)))
t[0,:] = 800
t[:,-1] = 20
A = np.zeros((len(r),len(r)))
B = np.zeros(len(r))
for i in range(int(xlast/dx)+1)[:-1]:
    eq_counter = 0
    for k in range(int(rlast/dr)+1)[1:-1]:
        A[eq_counter,k+1] = -Lambda*(1/r[k]+1/dr)
        A[eq_counter,k-1] = -Lambda*(1/dr)
        A[eq_counter,k] = Lambda*(1/r[k]+2/dr)+1
        t[i+1,0] = t[i+1,1]
        B[eq_counter]=t[i,k]
        eq_counter+=1
    A[eq_counter,1] = 1
    B[eq_counter] = t[i,2]
    eq_counter += 1
    A[eq_counter,-1] = 1
    B[eq_counter] = t[i,-1]
    t[i+1,:] = np.linalg.solve(A,B)
plt.figure(1)
plt.plot(x,t)
plt.figure(2)
x , r = np.meshgrid(x,r)
plt.contourf(x,r,np.transpose(t))