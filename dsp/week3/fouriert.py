import numpy as np
import matplotlib.pyplot as plt
l=int(input("Enter the length of discrete time signal"))
x=[]
for i in range(l):
	a=int(input("enter the discrete time signal"))
	x.append(a)
omega=np.arange(-np.pi,np.pi,0.00001*np.pi)
x=np.array(x)
X = np.zeros_like(omega, dtype=complex)
for k,w in enumerate(omega):
	for n in range(len(x)):
	    res=np.sum(x*np.exp(-1j*w*np.arange(len(x))))
	    X[k]=res
plt.subplot(2,1,1)
plt.plot(omega,np.abs(X))
plt.title("Magnitude of discrete time fourier transform")
plt.xlabel("Frequency (radians/samples)")
plt.subplot(2,1,2)
plt.plot(omega,np.angle(X))
plt.title("Phase Angle of discrete time fourier transform")
plt.xlabel("Frequency (radians/samples)")
plt.ylabel("phase(radians)")
plt.show()

