import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
lx=int(input("Enter length of x:"))
ly=int(input("Enter length of y:"))
print("Enter elements into x:")
for i in range(lx):
	a=int(input("Enter:"))
	x.append(a)
print("Enter elements into y:")
for i in range(ly):
	a=int(input("Enter:"))
	y.append(a)
z=[]
for k in range(ly-1):
	s=0
	for n in range(lx):
		if n+k<lx:
			s=s+x[n]*y[n+k]
	z.append(s)
plt.plot(z)
plt.xlabel('Lag')
plt.ylabel('cross-correlation')
plt.title('cross-correlation between x and y')
plt.show()
