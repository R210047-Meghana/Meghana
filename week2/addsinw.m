f1=1;
f2=2;
t=0:0.01:5;
x1=sin(2*pi*f1*t);
x2=sin(2*pi*f2*t);
y=x1+x2;
plot(t,y);
xlabel('Time');
ylabel('Amplitude');
title("addition of sine waves");






