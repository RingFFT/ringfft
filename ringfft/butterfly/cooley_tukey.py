# ringfft/butterfly/cooley_tukey.py
def butterfly(data, multiplier, modulo=None):
    assert len(data) == 2, "Data length must be exactly 2"
    a, b = data
    result = [(a + b * multiplier), (a - b * multiplier)]
    if modulo:
        result = [x % modulo for x in result]
    return result

