import argparse

from scipy.io.wavfile import read, write
import numpy as np
import matplotlib.pyplot as plt

from delay import process as delay
import lowpass

SAMPLE_RATE = 48000


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE] [FILE]...",
        description="Process waves"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('input', type=str)
    parser.add_argument('output', type=str)
    parser.add_argument("--effect", type=str, default="envelope", help="The type of processing to apply")

    return parser
def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()
    sample_rate, samples = read(args.input)

    scaled_samples = np.float32(samples / 32767.0)

    if args.effect == "lowpass":
        processed_samples = np.array(lowpass.process(scaled_samples, 40.0 / SAMPLE_RATE))
    else:
        processed_samples = np.array(delay(samples, 0.4))

    scaled_samples = np.int16(processed_samples * 32767)
    write(args.output, SAMPLE_RATE, scaled_samples)
    plt.plot(processed_samples)
    plt.show()

if __name__ == "__main__":
    main()



