t=0:1:5;
x=sin(0.2*pi*t);
y=cos(0.3*pi*t);
z=x+y;

figure; 
subplot(3,1,1); 
plot(t,x,'r')
title('x')
subplot(3,1,2);
plot(t,y,'b');
title("y")
subplot(3,1,3);
plot(t,z,'g')
title("z")