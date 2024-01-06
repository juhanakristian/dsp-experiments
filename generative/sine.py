import math

def generate_wavetable(sample_count: int) -> list[float]:
    """
    Generate sine wavetable
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    wavetable = []
    for i in range(sample_count):
        wavetable.append(math.sin((2 * math.pi) * (i / sample_count)))
    return wavetable

