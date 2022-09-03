# Faça um algoritmo para receber um número qualquer e informar na tela se é par ou ímpar. Utilize o operador %

valor = int(input("Digite um número: "))

if valor == 0:
    print("0 é um número neutro.")
elif valor % 2 == 0:
    print(valor, "é par.")
else:
    print(valor, "é ímpar.")