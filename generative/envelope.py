import typing

SAMPLE_RATE = 48000

class ADSR:
    attack: float # seconds
    decay: float # seconds
    sustain: float # amplitude
    release: float # seconds

    def __init__(self, attack: float, decay: float, sustain: float, release: float) -> None:
        self.attack = attack
        self.decay = decay
        self.sustain = sustain
        self.release = release


def process(samples: list[float], adsr: ADSR, gate: float) -> list[float]:
    """
    Simple ADSR envelope
    :param samples:
    :param adsr:
    :return:
    """
    attack_samples = int(adsr.attack * SAMPLE_RATE)
    decay_samples = attack_samples + int(adsr.decay * SAMPLE_RATE)
    release_samples = int(adsr.release * SAMPLE_RATE)

    gate_length = int(gate * SAMPLE_RATE)

    output = []
    current_amplitude = 0

    for i, sample in enumerate(samples):
        # Attach phase
        if i < attack_samples:
            current_amplitude += 1 / attack_samples
        # Decay phase
        elif i < decay_samples:
            current_amplitude -= (1 - adsr.sustain) / (decay_samples - attack_samples)
        # Release phase
        elif i > gate_length:
            current_amplitude -= adsr.sustain / release_samples

        current_amplitude = max(0, current_amplitude)
        output.append(sample * current_amplitude)

    return output