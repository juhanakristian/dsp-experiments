import numpy as np

def bandlimit_waveform(waveform_samples, sample_rate, nyquist):
    fft_result = np.fft.fft(waveform_samples)
    freqs = np.fft.fftfreq(len(waveform_samples), d=1/sample_rate)

    # Zeroing frequencies above the specified Nyquist frequency
    fft_result[np.abs(freqs) > nyquist] = 0

    # Inverse FFT to get the time-domain waveform
    bandlimited_waveform = np.fft.ifft(fft_result)
    # Clamp to -1 to 1
    bandlimited_waveform = np.clip(bandlimited_waveform, -1, 1)

    return np.real(bandlimited_waveform)  # Taking the real part


def create_wavetable(waveform_samples, sample_rate, levels):
    wavetable = []
    base_nyquist = sample_rate / 2

    for level in range(levels):
        nyquist = base_nyquist / (2 ** level)
        bandlimited_waveform = bandlimit_waveform(waveform_samples, sample_rate, nyquist)
        wavetable.append(bandlimited_waveform)

    return wavetable
