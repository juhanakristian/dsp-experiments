
def generate_wavetable(sample_count: int) -> list[float]:
    wavetable = []
    for i in range(sample_count):
        value = 1 if i < sample_count / 2 else -1
        wavetable.append(value)
    return wavetable


