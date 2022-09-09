#  Exibir os trinta primeiros valores da série de Fibonacci.

t1 = 0
t2 = 1
cont = 3

print("Os 30 primeiros números da sequência de Fibonacci são:")

print('{} -> {}'.format(t1, t2), end='')
while (cont <= 30):
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1