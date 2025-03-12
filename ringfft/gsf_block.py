# ringfft/gsf_block.py
from .fft_block_base import FFTBlock

class gsf(FFTBlock):
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

            # Gentleman–Sande 2點蝴蝶
            S = a + b
            D = (a - b)*w
            if self.reduction and self.modulo:
                S %= self.modulo
                D %= self.modulo
            data[idx_a] = S
            data[idx_b] = D


