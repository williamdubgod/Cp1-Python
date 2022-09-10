# Exibir os vinte primeiros valores da série de Bergamaschi. Use FOR.

a = -1
b = 1
c = 1
r = a + b + c

print("Os 20 primeiros números da sequência de Bergamaschi são:")

for i in range(1, 21, 1):
    print(r)
    c = b
    b = a
    a = r
    r = a + b + c
