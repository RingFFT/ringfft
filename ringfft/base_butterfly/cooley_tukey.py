# ringfft/butterfly/cooley_tukey.py
def Cooley_Tukey_base_btf(a, b, omega, modulo, reduction = True):
    """
    Perform the Cooley Tukey base butterfly, that is, performing 
    [a, b] -> [a + b * omega, a - b * omega]
    """
    result = [(a + b * omega), (a - b * omega)]

    if reduction:
        result = [x % modulo for x in result]
    return result


def Cooley_Tukey_btf(data, omegas, modulo, reduction = True):
    """
    Interpret data as a polynomial in R[x] / (x^n - 1), where  n = len(data) 
    and then perform a layer of Cooley Tukey butterfly, that is, 
    R[x] / (x^n - 1)   -> R[x] / (x^n/2 - 1)  X  R[x] / (x^n/2 + 1)
    """
    assert(len(data) % 2 == 0)
    

