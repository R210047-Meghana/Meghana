x=[]
y=[]
lx=input('Enter length of x:')
ly=input('Enter length of y:')
disp('Enter numbers into x:')
for i=1:lx
  a=input('Enter:')
  x=[x a]
endfor
disp('Enter elements into y:')
for i=1:ly
  a=input('Enter:')
  y=[y a]
endfor
z=[]
for k=0:ly-2
  s=0
  for n=1:lx
    if n+k<=lx
      s=s+x(n)*y(n+k)
    endif
  endfor
  z=[z s]
endfor
plot(z)
xlabel('Lag')
ylabel('cross-correlation')
title('cross-correlation between x and y')
