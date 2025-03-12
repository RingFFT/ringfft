# ringfft/ctf_block.py
from .fft_block_base import FFTBlock

class ctf(FFTBlock):
    def __init__(self, offset, length, omegas, reduction=False, modulo=None):
        self.offset = offset
        self.length = length
        self.omegas = omegas
        self.reduction = reduction
        self.modulo = modulo

    def apply(self, data):
        n_pairs = self.length // 2
        for i in range(n_pairs):
            idx_a = self.offset + 2*i
            idx_b = self.offset + 2*i + 1

            a = data[idx_a]
            b = data[idx_b]
            w = self.omegas[i] if i < len(self.omegas) else 1

            # Cooley–Tukey 2點蝴蝶
            A_prime = a + b*w
            B_prime = a - b*w
            if self.reduction and self.modulo:
                A_prime %= self.modulo
                B_prime %= self.modulo
            data[idx_a] = A_prime
            data[idx_b] = B_prime


