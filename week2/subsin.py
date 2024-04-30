import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,3,0.01)
f1=2
f2=4
x1=np.sin(2*np.pi*f1*t)
x2=np.sin(2*np.pi*f2*t)
x=x1-x2
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("addition of sine waves")
plt.show()
