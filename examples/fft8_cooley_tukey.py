import cmath
from ringfft.base_butterfly.cooley_tukey import Cooley_Tukey_base_btf

BIT_REVERSE_INDICES = [0, 4, 2, 6, 1, 5, 3, 7]


def fft8(data):
    """Compute an 8-point FFT using Cooley-Tukey butterflies."""
    data = [complex(data[i]) for i in BIT_REVERSE_INDICES]
    n = 8
    wn = cmath.exp(-2j * cmath.pi / n)

    # Stage 1
    for i in range(0, n, 2):
        data[i], data[i + 1] = Cooley_Tukey_base_btf(data[i], data[i + 1], 1, None, reduction=False)

    # Stage 2
    for i in range(0, n, 4):
        data[i], data[i + 2] = Cooley_Tukey_base_btf(data[i], data[i + 2], 1, None, reduction=False)
        data[i + 1], data[i + 3] = Cooley_Tukey_base_btf(data[i + 1], data[i + 3], wn ** 2, None, reduction=False)

    # Stage 3
    for i in range(0, n, 8):
        data[i],     data[i + 4] = Cooley_Tukey_base_btf(data[i],     data[i + 4], 1, None, reduction=False)
        data[i + 1], data[i + 5] = Cooley_Tukey_base_btf(data[i + 1], data[i + 5], wn, None, reduction=False)
        data[i + 2], data[i + 6] = Cooley_Tukey_base_btf(data[i + 2], data[i + 6], wn ** 2, None, reduction=False)
        data[i + 3], data[i + 7] = Cooley_Tukey_base_btf(data[i + 3], data[i + 7], wn ** 3, None, reduction=False)
    return data


def main():
    sample = list(range(8))
    result = fft8(sample)
    print("Input :", sample)
    print("Output:", result)


if __name__ == "__main__":
    main()
