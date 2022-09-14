#  Crie um programa em que o usuário entre com um número inteiro qualquer, e o programa imprima os 20 números subsequentes ao que foi digitado pelo usuário.

numero = int(input("Digite um número inteiro: "))

for i in range(1, 20, 1):
    numero += 1
    print(numero)