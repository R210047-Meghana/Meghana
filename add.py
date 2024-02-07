a=input('enter first number')
b=input('enter second number')
if (type(a)==int or float):
	if (type(b)==int or float):
		div=(float(a)/float(b))
		print('div=',div)
else:
	print('error')
	
	
	
	
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
		
		
		
		
def dete(matrix):
	if(len(matrix))==2 and len(matrix[0])==2:
		return(matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
	if(len(matrix)!=len(matrix[0])):
		return 'the matrix must be square'
	det=0
	for j in range(len(matrix[0])):
		cofactor=(-1)**j*matrix[0][j]
		submatrix=[[matrix[i][k] for k in range(len(matrix[0])) if k!=j] for i in range(1,len(matrix))]
		subdet=dete(submatrix)
		det+=cofactor*subdet
	return det

matrix=[[1,2,3],
	[4,5,6],
	[7,8,9]]
det=dete(matrix)
print('the determinant of the matrix is:',det)
		
		
		
		
		
		

