import numpy as np
from matplotlib import pyplot as plt
x=[1,2,3,4,5]
l=2
downsampled_x=x[::l]
print(downsampled_x)
plt.subplot(2,1,1)
plt.stem(x)
plt.subplot(2,1,2)
plt.stem(downsampled_x)
plt.show()

