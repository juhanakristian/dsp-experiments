import numpy as np

fs = 48000  # Sampling rate

def generate_waveform(sample_count: int) -> list[float]:
    """
    Generate noise waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    white_noise = np.random.uniform(low=-1, high=1, size=sample_count)
    return list(white_noise)
