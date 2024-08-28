import numpy as np
import matplotlib.pyplot as plt
def dft(x,N):
	X=[]
	for k in np.arange(0,N):
		s=0
		for n in np.arange(0,N):
			s=s+x[n]*np.exp(-1j*2*np.pi*k*n/N)
		X.append(s)
	return X
	
n=np.arange(0,1800)
x=np.cos(2*np.pi*50*n/1800)
N=len(n)
X=dft(x,N)
plt.subplot(2,1,1)
plt.plot(n,np.abs(X))
plt.title("Magnitude of discrete fourier transform")
plt.xlabel("Frequency (radians/samples)")
plt.subplot(2,1,2)
plt.plot(n,np.angle(X))
plt.title("Phase Angle of discrete fourier transform")
plt.xlabel("Frequency (radians/samples)")
plt.ylabel("phase(radians)")
plt.show()


peak=np.max(abs(np.array(X)))
print("peak=")
print(peak)
