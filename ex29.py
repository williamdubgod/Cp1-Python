#  Faça um algoritmo que leia uma variável e some 5 caso seja par ou some 8 caso seja ímpar, imprimir o resultado desta operação.

valor = int(input("Digite um número: "))

if valor % 2 == 0:
    print(valor + 5)
else:
    print(valor + 8)
