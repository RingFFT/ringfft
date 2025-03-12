# ringfft/fft_circuit.py

from typing import List, Union
from .fft_block_base import FFTBlock

class FFTCircuit:
    """
    用來串接多個 FFTBlock 的管線 (或電路)。
    """

    def __init__(self):
        self.steps: List[Union[FFTBlock, str]] = []

    def add(self, step: Union[FFTBlock, str]):
        """
        step 可以是:
          - 繼承自 FFTBlock 的物件 (ctf, gsf, 其他 block)
          - 字串 "printout" (或其他關鍵字) 做特別動作
        """
        self.steps.append(step)

    def run(self, data):
        for i, step in enumerate(self.steps):
            if isinstance(step, FFTBlock):
                # 正統 FFTBlock => 呼叫 apply()
                step.apply(data)
            elif isinstance(step, str):
                # 特殊處理
                if step == "printout":
                    print(f"Step {i} => {data}")
                else:
                    print(f"[Warning] Unknown string step: {step}")
            else:
                print(f"[Error] Unknown step type: {type(step)}")

        return data

