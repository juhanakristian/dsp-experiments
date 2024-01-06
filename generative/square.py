
def simple_square(sample_count: int) -> list[float]:
    """
    Generate square waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    waveform = []
    for i in range(sample_count):
        value = 1 if i < sample_count / 2 else -1
        waveform.append(value)
    return waveform


def bandlimited_square(sample_count: int, frequency: int) -> list[float]:
    """
    Generate bandlimited square waveform by computing the Fourier series
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    waveform = []

