from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 48000

sample_rate, samples = read("input.wav")

DELAY_LINE_SIZE = SAMPLE_RATE * 2

def process(samples: list[float], mix: float = 0.8) -> list[float]:
    """
    Simple delay
    :param samples: A list of samples between -1 and 1
    :return: A list of samples between -1 and 1
    """
    output = []
    delay_line = [0] * DELAY_LINE_SIZE
    feedback = 0.8
    dry_mix = 1 - mix
    delay_index = 0
    for i, sample in enumerate(samples):
        # Get value from delay line and mix it with sample value
        delayed_value = delay_line[delay_index]
        value = (sample * dry_mix) + (delayed_value * mix)
        output.append(value)

        # Update delay line
        delay_line[delay_index] = (sample + delayed_value) * feedback
        delay_index += 1
        if delay_index >= DELAY_LINE_SIZE:
            delay_index = 0

    return output


def main() -> None:
    processed_samples = np.array(process(samples, 0.4))
    scaled_samples = np.int16(processed_samples * 32767)
    write("output-delay.wav", SAMPLE_RATE, scaled_samples)
    plt.plot(processed_samples)
    plt.show()


if __name__ == "__main__":
    main()



