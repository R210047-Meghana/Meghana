from matplotlib import pyplot as plt
x=[1,2,3,4,5]
y=[]
le=len(x)-1
l=3
r=l*le+1
for i in range(0,r):
    if(i%l==0):
          y.append(x[int(i/l)])
    else:
          y.append(0)
for i in range(0,r):
    print(y[i],end=',')
plt.plot(y[i])
plt.show()
