
def generate_wavetable(sample_count: int) -> list[float]:
    """
    Generate square wavetable
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    wavetable = []
    for i in range(sample_count):
        value = 1 if i < sample_count / 2 else -1
        wavetable.append(value)
    return wavetable


