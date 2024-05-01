[x, fs] = audioread('/home/rguktrkvalley/Pictures/enough.jpeg');
t = (0:length(x)-1) / fs; 
plot(t, x);
xlabel('Time (seconds)');
ylabel('Amplitude');
title('Audio Waveform');