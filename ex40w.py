#  Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla. Use While.

i = 1
j = 1

while (i <= 20):
    while (j <= 10):
        t = i * j
        print(i, ' X ', j, ' = ', t)
        j += 1
    j = 1
    i += 1
    input("Digite qualquer tecla para continuar...")