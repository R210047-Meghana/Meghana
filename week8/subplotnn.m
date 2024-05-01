audiofile = '/home/rguktrkvalley/Downloads/file_example_WAV_1MG.wav';
[audioData, sampleRate] = audioread(audiofile);
numchannels = size(audioData, 2);
time = (0:size(audioData, 1)-1) / sampleRate;

figure;

if numchannels == 1
    plot(time, audioData);
    xlabel('Time (s)');
    ylabel('Amplitude');
    title('Mono Audio');
else
    subplot(2,1,1);
    plot(time, audioData(:, 1));
    xlabel('Time (s)');
    ylabel('Amplitude');
    title('Channel 1');
    
    subplot(2,1,2);
    plot(time, audioData(:, 2));
    xlabel('Time (s)');
    ylabel('Amplitude');
    title('Channel 2'); 
end
