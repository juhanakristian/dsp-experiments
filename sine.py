import math
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np

SAMPLE_RATE = 48000
def generate_wavetable(sample_count: int) -> list[float]:
    wavetable = []
    for i in range(sample_count):
        wavetable.append(math.sin((2 * math.pi) * (i / sample_count)))
    return wavetable

def sine(frequency: int, duration: int) -> list[float]:
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



samples = np.array(sine(440, 1))

write("example.wav", 48000, samples.astype(np.int16))
plt.plot(generate_wavetable(1000))
plt.show()

