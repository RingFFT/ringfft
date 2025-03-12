# ringfft/fft_block_base.py
from abc import ABC, abstractmethod

class FFTBlock(ABC):
    """
    抽象類別，表示"可對 data 做一次 FFT/NTT 階段運算"的 block。
    """
    @abstractmethod
    def apply(self, data):
        """
        對 data 進行運算/轉換。
        """
        pass

