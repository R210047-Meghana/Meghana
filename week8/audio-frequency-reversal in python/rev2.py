from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
fs, x = wavfile.read('/home/rguktrkvalley/Downloads/file_example_WAV_1MG.wav')
t = np.arange(0, len(x)) / fs
plt.plot(t, x)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Audio Waveform')
plt.show()
