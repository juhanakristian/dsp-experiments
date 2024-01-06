
def simple_sawtooth(sample_count: int) -> list[float]:
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
    return waveform
