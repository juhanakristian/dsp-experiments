from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import argparse

import sine
import square
import impulse

SAMPLE_RATE = 48000


def init_argparse() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        usage="%(prog)s [OPTION] [FILE]...",
        description="Generate waves"
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version = f"{parser.prog} version 1.0.0"
    )
    parser.add_argument('output', type=str)
    parser.add_argument("--wave", type=str, default="sine", help="The type of wave to generate")
    parser.add_argument("--frequency", type=int, default=440, help="The frequency of the wave")
    parser.add_argument("--duration", type=int, default=1, help="The duration of the wave in seconds")
    parser.add_argument("--oneoff", type=bool, default=False, help="Whether to generate a one-off wave or not")

    return parser


def generate(frequency: int, duration: int, wavetable: list[float]) -> list[float]:
    sample_count = SAMPLE_RATE * duration

    samples = []
    phase = 0
    step = frequency * (len(wavetable) / SAMPLE_RATE)
    amplitude = np.iinfo(np.int16).max
    for i in range(sample_count):
        samples.append(wavetable[int(phase)] * amplitude)
        phase += step
        phase %= len(wavetable)

    return samples


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()

    wavetable = []
    if args.wave == "sine":
        wavetable = sine.generate_wavetable(1000)
    elif args.wave == "square":
        wavetable = square.generate_wavetable(1000)
    elif args.wave == "impulse":
        wavetable = impulse.generate_wavetable(1000)

    if not args.oneoff:
        samples = np.array(generate(args.frequency, args.duration, wavetable))
    else:
        rest = [0] * (SAMPLE_RATE * args.duration)
        samples = np.array(wavetable + rest)
    scaled_samples = np.int16(samples * 32767)
    write(args.output, SAMPLE_RATE, scaled_samples)
    plt.plot(wavetable)
    plt.show()


if __name__ == "__main__":
    main()

