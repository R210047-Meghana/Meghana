#sum of two numbers


a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=a+b
print(c)



#division of two numbers


a=input('enter number a:')
b=input('enter number b:')
acopy=a.replace("."," ")
bcopy=b.replace("."," ")
if((a.isnumeric() or acopy.isnumeric()) and (b.isnumeric() or bcopy.isnumeric())):
	print(float(a)/float(b))
else:
	print("enter a numerical value")
	
	
	
	
#dot product of two vectors




l=[]
m=[]
s=0
n=int(input('length of vector'))
for i in range(n):
	a=int(input('enter number'))
	b=int(input('enter another number'))
	l.append(a)
	m.append(b)
print('list l=',l)
print('list m=',m)
for i in range(len(l)):
	s=s+l[i]*m[i]
print('dot product of two vectors=',s)
		
		
		
		
#find the determinant of the matrix
		
import numpy as np
n_array=np.array([[1,2,3],[4,7,6],[7,8,9]])
print('numpy matrix is:')
print(n_array)
det=np.linalg.det(n_array)
print('det of matrix:',int(det))
		
		
		
#addition of matrices


a=[[9,2,8],[4,5,6],[9,3,2]]
b=[[1,2,3],[4,5,6],[7,8,9]]
c=[[4,9,6],[2,4,0],[1,0,6]]
d=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
	for j in range(len(a[0])):
		d[i][j]=a[i][j]+b[i][j]+c[i][j]
for row in d:
	print(row)
