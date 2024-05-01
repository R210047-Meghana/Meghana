
[x, fs] = audioread('/home/rguktrkvalley/Pictures/enough.jpeg');
x_reverse = flipud(x);
audiowrite('n.wav', x_reverse, fs);



