import numpy as np
from matplotlib import pyplot as plt
a={1,2,3,4,5}
b=[]
s=0
for i in  a:
     s=s+i
     b.append(s)
print(b)
plt.plot(b)
plt.show()
