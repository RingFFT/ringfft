# examples/simple_example.py
from ringfft import ctb

data = [3, 5]
multiplier = 2
modulo = 17

result = ctb(data, multiplier, modulo)
print("輸入：", data)
print("結果：", result)

