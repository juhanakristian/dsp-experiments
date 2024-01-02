import math

def generate_wavetable(sample_count: int) -> list[float]:
    """
    Generate impulse wavetable
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    wavetable = [
        1 if i < 10 else 0
        for i in range(sample_count)
    ]
    return wavetable
