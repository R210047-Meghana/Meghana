function [t,x] = gensin(f)
  t=0:0.01:1
  f=3;
  x=sin(2*pi*f*t)
  plot(t,x)
end
gensin(f);

