function dydt=model(t,y)
  dydt = (1-y)/(1.95-y)-y/(0.05+y);
end

y0=[0,1,2]
t=linspace(1,10)
(t,y)=ode45(@model,t,y0);
plot(t,y)
xlabel('Time');
ylabel('Amplitude')
title('solution of dydt = (1-y)/(1.95-y)-y/(0.05+y)')
