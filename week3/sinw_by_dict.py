import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin_dict={'s1':[2,5],'s2':[5,10],'s3':[3,7],'s4':[10,2],'s5':[1,2]}

print("choose: {'s1':[2,5],'s2':[5,10],'s3':[3,7],'s4':[10,2],'s5':[1,2]}") 
k=input("Enter sinusoidal key to generate:")
if sin_dict[k]:
    x=sin_dict[k][0]*np.sin(2*np.pi*sin_dict[k][1]*t)
    plt.plot(t,x);plt.xlabel('Time');plt.ylabel('Amplitude');plt.title(["sinusoidal signal:",k])
    plt.show()
    
