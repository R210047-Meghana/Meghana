from scipy.io import wavfile

x,f=wavfile.read('/home/rguktrkvalley/Downloads/file_example_WAV_1MG.wav')

print('sample rate:',x,'Hz')
print('Number of samples:',len(f))
