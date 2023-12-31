import math

def generate_wavetable(sample_count: int) -> list[float]:
    wavetable = []
    for i in range(sample_count):
        wavetable.append(math.sin((2 * math.pi) * (i / sample_count)))
    return wavetable

