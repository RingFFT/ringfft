# demo.py
from ringfft import FFTCircuit, ctf, gsf

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8]

    omegas_len2  = [1]
    omegas_len4  = [1, 3]
    omegas_len8  = [1, 2, 3, 4]

    my_circuit = FFTCircuit()

    # 加 ctf blocks
    my_circuit.add("printout")
    my_circuit.add(ctf(offset=0, length=8, omegas=omegas_len8, reduction=False))
    my_circuit.add("printout")
    my_circuit.add(ctf(offset=0, length=4, omegas=omegas_len4, reduction=False))
    my_circuit.add(ctf(offset=4, length=4, omegas=omegas_len4, reduction=False))

    my_circuit.add("printout")
    my_circuit.add(ctf(offset=0, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(ctf(offset=2, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(ctf(offset=4, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(ctf(offset=6, length=2, omegas=omegas_len2, reduction=False))

    my_circuit.add("printout")

    # 加 gsf blocks
    my_circuit.add(gsf(offset=0, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(gsf(offset=2, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(gsf(offset=4, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add(gsf(offset=6, length=2, omegas=omegas_len2, reduction=False))
    my_circuit.add("printout")

    my_circuit.add(gsf(offset=0, length=4, omegas=omegas_len4, reduction=False))
    my_circuit.add(gsf(offset=4, length=4, omegas=omegas_len4, reduction=False))
    my_circuit.add("printout")

    my_circuit.add(gsf(offset=0, length=8, omegas=omegas_len8, reduction=False))

    result = my_circuit.run(data)
    print("Final Result =>", result)

if __name__ == "__main__":
    main()

