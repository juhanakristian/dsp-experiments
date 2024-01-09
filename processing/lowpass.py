import math


def process(samples: list[float], cutoff: float) -> list[float]:
    """
    Simple lowpass filter
    :param samples: A list of samples between -1 and 1
    :param cutoff: Cutoff frequency in Hz
    :return: A list of samples between -1 and 1
    """
    # Calculate coefficients
    b1 = math.exp(-2.0 * math.pi * cutoff)
    a0 = 1.0 - b1

    z1 = 0.0
    output = []
    for sample in samples:
        r = sample * a0 + z1 * b1
        output.append(-r)
        z1 = r

    return output




