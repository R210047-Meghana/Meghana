clear all;
close all;
clc;
function [t,x] = gensin(f)
  t=0:0.01:1
  x=sin(2*pi*f*t)
  plot(t,x)
end
f=3;
gensin(f);

