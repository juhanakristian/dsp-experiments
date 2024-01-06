import numpy as np
import matplotlib.pyplot as plt


def bandlimit_waveform(waveform_samples, sample_rate, nyquist):
    fft_result = np.fft.fft(waveform_samples)
    freqs = np.fft.fftfreq(len(waveform_samples), d=1/sample_rate)

    # Zeroing frequencies above the specified Nyquist frequency
    fft_result[np.abs(freqs) > nyquist] = 0

    # Inverse FFT to get the time-domain waveform
    bandlimited_waveform = np.fft.ifft(fft_result)
    return np.real(bandlimited_waveform)  # Taking the real part

def create_wavetable(waveform_samples, sample_rate, levels):
    wavetable = []
    base_nyquist = sample_rate / 2

    for level in range(levels):
        nyquist = base_nyquist / (2 ** level)
        bandlimited_waveform = bandlimit_waveform(waveform_samples, sample_rate, nyquist)
        wavetable.append(bandlimited_waveform)

    return wavetable

def simple_waveform(sample_count: int) -> list[float]:
    """
    Generate square waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    waveform = []
    step = 2.0 / sample_count
    for i in range(sample_count):
        value = 1 - (i * step)
        waveform.append(value)
    return [-1] + waveform + [1]
def bandlimited_waveform(sample_count: int) -> list[float]:
    """
    Generate bandlimited square waveform using FFT
    :param sample_count: Number of samples
    :param frequency: Base frequency of the waveform (needed to calculate the harmonics)
    :return: A list of samples between -1 and 1
    """
    waveform = simple_waveform(sample_count)
    wavetable = create_wavetable(waveform, 48000 / 2, levels=8)
    last = wavetable[-1]
    #plot
    plt.plot(last)
    plt.show()
    return last



