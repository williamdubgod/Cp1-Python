# Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cinqüenta. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A sequencia: 1/2, 2/3, 3/4, 4/5...

n = int(input("Digite um número positivo e memor que 100: "))

while n < 0 or n >= 50:
    print("O número deve ser positivo e menor que 50")
    n = int(input("Digite novamente: "))

a = 1
b = 2
i = 1

while i <= n:
    print(f"{a}/{b}")
    a += 1
    b += 1
    i += 1


