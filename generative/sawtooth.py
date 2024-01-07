import numpy as np
import matplotlib.pyplot as plt

from wavetable import create_wavetable

SAMPLE_COUNT = 2048
SAMPLING_RATE = 48000

def simple_waveform() -> list[float]:
    """
    Generate square waveform
    :param sample_count: Number of samples
    :return: A list of samples between -1 and 1
    """
    waveform = []
    step = 1.0 / SAMPLE_COUNT
    for i in range(SAMPLE_COUNT):
        value = 0.5 - (i * step)
        waveform.append(value)

    return waveform


def generate(frequency: int) -> list[float]:
    """
    Generate bandlimited square waveform using FFT
    :param frequency: Frequency of the waveform (needed to calculate the removed harmonics)
    :return: A list of samples between -1 and 1
    """
    waveform = simple_waveform()
    wavetable = create_wavetable(waveform, SAMPLING_RATE, levels=8)

    return wavetable


