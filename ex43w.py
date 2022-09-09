# Exibir os vinte primeiros valores da série de Bergamaschi. Use While.

t1 = 1
t2 = 1
t3 = 1
cont = 3

print("Os 20 primeiros números da sequência de Bergamaschi são:")

print('{} -> {}'.format(t1, t2, t3), end='')
while (cont <= 20):
    t4 = t1 + t2 + t3
    print(' -> {}'.format(t4), end='')
    t1 = t2
    t2 = t3
    t3 = t4
    cont += 1