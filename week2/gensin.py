import numpy as np
import matplotlib.pyplot as plt
t=np.arange(0,1,0.01)
f=3
x=np.sin(2*np.pi*f*t)
plt.plot(t,x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title("sine wave")
plt.grid(True)
plt.show()

