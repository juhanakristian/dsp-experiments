import numpy as np

def bandlimit_waveform(waveform_samples, sample_rate, max_harmonics):
    fft_result = np.fft.fft(waveform_samples)
    freqs = np.fft.fftfreq(len(waveform_samples), d=1/sample_rate)

    # Remove harmonics above the max_harmonics
    nyquist = max_harmonics * (sample_rate / 2) / len(waveform_samples)
    # Zeroing frequencies above the specified Nyquist frequency
    fft_result[np.abs(freqs) > nyquist] = 0

    # Inverse FFT to get the time-domain waveform
    bandlimited_waveform = np.fft.ifft(fft_result)
    # Clamp to -1 to 1
    bandlimited_waveform = np.clip(bandlimited_waveform, -1, 1)

    return np.real(bandlimited_waveform)  # Taking the real part


def create_wavetable(waveform_samples, sample_rate, levels):
    wavetable = []

    max_harmonics = 368
    for level in range(levels):
        bandlimited_waveform = bandlimit_waveform(waveform_samples, sample_rate, max_harmonics)
        wavetable.append(bandlimited_waveform)
        max_harmonics = max_harmonics // 2

    return wavetable


def interpolate(waveform_a: list[float], waveform_b: list[float], ratio: float) -> list[float]:
    """
    Interpolate between two waveforms
    :param waveform_a: First waveform
    :param waveform_b: Second waveform
    :param ratio: Ratio of interpolation
    :return: A list of samples between -1 and 1
    """
    waveform = []
    for i in range(len(waveform_a)):
        value = (waveform_a[i] * (1 - ratio)) + (waveform_b[i] * ratio)
        waveform.append(value)
    return waveform


def freq_waveform(frequency: int, wavetable: list[list[float]]) -> list[float]:
    # Select correct wavetable  and interpolate
    top_frequency = 40
    previous_top_frequency = 40
    for i in range(len(wavetable)):
        if frequency <= top_frequency and i > 0:
            return wavetable[i]
            #ratio = (frequency - previous_top_frequency) / (top_frequency - previous_top_frequency)
            #print(f"Interpolating between {previous_top_frequency} and {top_frequency} with ratio {ratio}")
            #return interpolate(wavetable[i - 1], wavetable[i], ratio)
        #previous_top_frequency = top_frequency
        top_frequency = top_frequency * 2
    return wavetable[-1]
