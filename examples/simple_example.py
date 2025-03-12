# examples/simple_example.py
from ringfft import ctb

data = [3, 5]
multiplier = 2
modulo = 17

result = ctb(data, multiplier, modulo)
print("輸入：", data)
print("結果：", result)



data = [1, 2, 3, 4, 5, 6, 7, 8] 

my_FFT = FFTBlock()

my_FFT.add( ctf(offset = 0, length = 8, omegas = [powers of root of unity], reduction = False ) )

my_FFT.add( ctf(offset = 0, length = 4, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( ctf(offset = 4, length = 4, omegas = [powers of root of unity], reduction = False ))

my_FFT.add( ctf(offset = 0, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( ctf(offset = 2, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( ctf(offset = 4, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( ctf(offset = 6, length = 2, omegas = [powers of root of unity], reduction = False ))

my_FFT.add( "printout" )


my_FFT.add( gsf(offset = 0, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( gsf(offset = 2, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( gsf(offset = 4, length = 2, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( gsf(offset = 6, length = 2, omegas = [powers of root of unity], reduction = False ))


my_FFT.add( gsf(offset = 0, length = 4, omegas = [powers of root of unity], reduction = False ))
my_FFT.add( gsf(offset = 4, length = 4, omegas = [powers of root of unity], reduction = False ))


my_FFT.add( gsf(offset = 0, length = 8, omegas = [powers of root of unity], reduction = False ))


my_FFT.run(data = data)

