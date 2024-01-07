from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
import argparse

import noise
import sine
import square
import impulse
import sawtooth
from wavetable import freq_waveform

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
    parser.add_argument("--sweep", type=bool, default=False, help="Whether to generate a sweep or not")

    return parser


def generate(frequency: int, duration: int, wavetable: list[float]) -> list[float]:
    sample_count = SAMPLE_RATE * duration

    samples = []
    phase = 0
    step = frequency * (len(wavetable) / SAMPLE_RATE)
    for i in range(sample_count):
        samples.append(wavetable[int(phase)])
        phase += step
        phase %= len(wavetable)

    return samples


def sweep(frequency_start: int, frequency_end: int, duration: int, wavetable: list[list[float]]) -> list[float]:
    sample_count = SAMPLE_RATE * duration

    samples = []
    phase = 0
    step = (frequency_end - frequency_start) / sample_count
    frequency = frequency_start
    for i in range(sample_count):
        waveform = freq_waveform(frequency, wavetable)
        samples.append(waveform[int(phase)])
        phase += frequency * (len(waveform) / SAMPLE_RATE)
        frequency += step
        phase %= len(waveform)

    return samples


def main() -> None:
    parser = init_argparse()
    args = parser.parse_args()

    sample_count = 2048

    wavetable = []
    if args.wave == "sine":
        wavetable = sine.generate_wavetable(sample_count)
    elif args.wave == "square":
        wavetable = square.simple_square(sample_count)
    elif args.wave == "sawtooth":
        wavetable = sawtooth.generate(args.frequency)
    elif args.wave == "impulse":
        wavetable = impulse.generate_wavetable(sample_count)
    elif args.wave == "noise":
        wavetable = noise.generate_waveform(SAMPLE_RATE * args.duration)

    samples = []
    if args.sweep:
        samples = np.array(sweep(40, 8000, args.duration, wavetable))
    elif args.oneoff:
        rest = [0] * (SAMPLE_RATE * args.duration)
        samples = np.array(wavetable + rest)
    elif not args.wave != "noise":
        samples = np.array(generate(args.frequency, args.duration, wavetable))

    if len(samples) == 0:
        return

    scaled_samples = np.int16(samples * 32767)
    write(args.output, SAMPLE_RATE, scaled_samples)
    plt.plot(wavetable)
    plt.show()


if __name__ == "__main__":
    main()

