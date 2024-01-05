import numpy as np


def generate_waveform(sample_count: int) -> list[float]:
    """
    Generate noise waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    return np.random.uniform(low=-1, high=1, size=sample_count) * 0.2