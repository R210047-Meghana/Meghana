import numpy as np
import matplotlib.pyplot as plt
x1=np.array([1,2,3,4,5])
x2=np.array([1,2,3,4,5])
omega=np.linspace(-np.pi,np.pi,1000)
omega1=np.array([np.sum(x1*np.exp(-1j*k*np.arange(5))) for k in omega])
omega2=np.array([np.sum(x2*np.exp(-1j*k*np.arange(5))) for k in omega])
x3=omega1.all()*omega2.all()
con=np.convolve(x1,x2,mode="full")
if(x3.all()==con.all()):
    print("convolution is verified")
else:
    print("convolution is not verified")

