import math
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

SAMPLE_RATE = 48000
def generate_wavetable(sample_count: int) -> list[float]:
    wavetable = []
    for i in range(sample_count):
        value = 1 if i < sample_count / 2 else -1
        wavetable.append(value)
    return wavetable

def square(frequency: int, duration: int) -> list[float]:
    sample_count = SAMPLE_RATE * duration

    wavetable = generate_wavetable(1000)
    samples = []
    phase = 0
    step = frequency * (len(wavetable) / SAMPLE_RATE)
    amplitude = np.iinfo(np.int16).max
    for i in range(sample_count):
        samples.append(wavetable[int(phase)] * amplitude)
        phase += step
        phase %= len(wavetable)

    return samples



samples = np.array(square(440, 1))

write("square.wav", 48000, samples.astype(np.int16))
plt.plot(generate_wavetable(1000))
plt.show()

