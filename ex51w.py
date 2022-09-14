#  Crie um programa em que o usuário entre com um número inteiro qualquer, e o programa imprima os 20 números subsequentes ao que foi digitado pelo usuário. Use while.

numero = int(input("Digite um número inteiro: "))

i = 1

while i < 20:
    numero += 1
    print(numero)
    i += 1