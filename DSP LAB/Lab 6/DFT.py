import numpy as np
import matplotlib.pyplot as plt
x=[1,2,-1,3]
N=len(x)

f=[]
omega=np.arange(0,2*np.pi,(2*np.pi/len(x)))
for i in range(0,N):
    X=[]
    for k in range(0,N):
        a=x[i]*np.exp((-1j*(2*np.pi*k*i))/N)
        X.append(a)
    f.append(sum(X))
print(f)
plt.xlabel("Omega")
plt.ylabel("Amplitude")
plt.stem(omega,np.angle(f))
plt.show()
