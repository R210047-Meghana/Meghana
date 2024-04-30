%addition of 2 numbers


a=input('Enter a:');
b=input('Enter b:');
c=a+b;
disp(c);



% division of two numbers


a=input('Enter a:','s');
b=input('Enter b:','s');
if all(isstrprop(a,'digit')) && all(isstrprop(b,'digit'))
  disp(a/b)
else
  disp('Enter a numrical value')
end


%dot product of two numbers


m=[];
k=[];
s=0;
n=input('Enter number of dimensions of vector:');
for i=1:n
  a=input('Enter co-efficient of vector a:');
  b=input('Enter co-efficient of vector b:');
  m(i)=a;
  k(i)=b; 
end
disp('vector1=');
disp(m);
disp('vector2=');
disp(k);
for i=1:length(m)
  s=s+m(i)*k(i);
end
fprintf('dot product=%d \n',s)


%determinant of matrix


matrix=[1,2,3;4,5,6;7,8,9]
determinant=det(matrix);
disp(determinant);



%addition of matrices



A=[1,2,3;4,5,6;7,8,9];
B=[4,5,6;2,4,5;1,4,3];
C=A+B;
disp('matrix A:');
disp(A);
disp('matrix b:');
disp(B);
disp('matrix C=(A+B):');
disp(C);