#  Exibir os trinta primeiros valores da série de Fibonacci. Use FOR

a = 0
b = 1
f = a + b

for i in range(1, 31, 1):
    print(f)
    b = a
    a = f
    f = a + b