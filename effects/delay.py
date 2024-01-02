from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

SAMPLE_RATE = 48000

sample_rate, samples = read("input.wav")

def process(samples: list[float], amount: float, attenuation: float = 0.8) -> list[float]:
    """
    Simple delay
    :param samples: A list of samples between -1 and 1
    :return: A list of samples between -1 and 1
    """
    output = []
    sample_amount = round(amount * sample_rate)
    for i, sample in enumerate(samples):
        delayed_sample = samples[i - sample_amount] if i - sample_amount > 0 else 0
        #value = sample + delayed_sample * attenuation
        value = min(max(sample + delayed_sample * attenuation, -1), 1)
        output.append(value)

    return output


def main() -> None:
    processed_samples = np.array(process(samples, 0.24, 0.4))
    write("output-delay.wav", SAMPLE_RATE, processed_samples.astype(np.int16))
    plt.plot(processed_samples)
    plt.show()


if __name__ == "__main__":
    main()



