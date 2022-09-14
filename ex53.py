# Elabore um programa que apresente os números pares maiores que 10 no intervalo fechado [A, B]. Sendo que A e B serão números inteiros escolhidos pelo usuário.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n1 >= n2:
    print("O segundo número deve ser maior que o primeiro!")
    n2 = int(input("Digite novamente o segundo número: "))

for i in range(n1, n2 + 1, 1):
    if i > 10 and i % 2 == 0:
        print(i)
    n1 = n2
    n2 += 1