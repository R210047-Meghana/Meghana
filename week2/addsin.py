import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,5,0.01)
f1=1
f2=2
x1=np.sin(2*np.pi*f1*t)
x2=np.sin(2*np.pi*f2*t)
x=x1+x2
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("addition of sine waves")
plt.show()
