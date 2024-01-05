import numpy as np
from scipy.signal import butter, filtfilt

fs = 48000  # Sampling rate
cutoff = 5000
# Butterworth low-pass filter
def butter_lowpass_filter(data, cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = filtfilt(b, a, data)
    return y

# Apply low-pass filter

def generate_waveform(sample_count: int) -> list[float]:
    """
    Generate noise waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    white_noise = np.random.uniform(low=-1, high=1, size=sample_count)
    filtered_noise = butter_lowpass_filter(white_noise, cutoff, fs)
    filtered_noise /= np.max(np.abs(filtered_noise))
    return list(filtered_noise)
