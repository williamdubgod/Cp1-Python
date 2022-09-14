#  Crie um programa que solicite que o usuário entre com dois números (inicial e final). Ao final o programa deverá apresentar o valor total da soma de todos os números do intervalo digitado pelo usuário. Use for

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

while n1 >= n2:
    print("O segundo número deve ser maior que o primeiro!")
    n2 = int(input("Digite novamente o segundo número: "))

for i in range(n1, n2, 1):
    soma = n1 + n2
    n1 = n2
    n2 += 1
print(soma)