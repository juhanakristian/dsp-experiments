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

def interpolate(waveform_a: list[float], waveform_b: list[float], ratio: float) -> list[float]:
    """
    Interpolate between two waveforms
    :param waveform_a: First waveform
    :param waveform_b: Second waveform
    :param ratio: Ratio of interpolation
    :return: A list of samples between -1 and 1
    """
    waveform = []
    for i in range(len(waveform_a)):
        value = (waveform_a[i] * (1 - ratio)) + (waveform_b[i] * ratio)
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
    # Select correct wavetable  and interpolate
    for i in range(len(wavetable)):
        top_frequency = 40 * (2 ** i)
        if frequency <= top_frequency:
            print(f"Using wavetable {i}")
            previous_top_frequency = 40 * (2 ** (i - 1))
            ratio = (frequency - previous_top_frequency) / (top_frequency - previous_top_frequency)
            return interpolate(wavetable[i-1], wavetable[i], ratio)

    return wavetable[-1]



