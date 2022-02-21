#kushal Kharel 
#problem 3


import numpy as np
import matplotlib.pyplot as plt
Fs = 500 # sample rate
Ts = 1/Fs # sample period
N = 2048 # number of samples to simulate
t = Ts*np.arange(N)
S1 = 200*np.exp(1j*2*np.pi*100*t) # simulates sinusoid at 100 Hz


S2 = 20*np.exp(1j*2*np.pi*200*t) # simulates sinusoid at 50 Hz

TransmittedX = S1 + S2 #combining the 2 signals

noise = (np.random.randn(N) + 1j*np.random.randn(N))/np.sqrt(2) #random noise unity power

ReceivedX = TransmittedX + noise #adding noise to the combined signal

PSD = (np.abs(np.fft.fft(ReceivedX))/N)**2 #calculating PSD

PSD_log = 10.0*np.log10(PSD) #converting to log scale

PSD_shifted = np.fft.fftshift(PSD_log) #shifting the psd log

#arranging and plotting the signal
f = np.arange(Fs/-2.0, Fs/2.0, Fs/N) # start, stop, step
plt.plot(f, PSD_shifted)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.grid(True)
plt.show()
