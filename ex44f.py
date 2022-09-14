# Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cem. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A seqüência: 2, 5, 10, 17, 26, .... Use for

n = int(input("Digite um número positivo e memor que 100: "))

while n < 0 or n > 100:
    print("O número deve ser positivo e menor que 100")
    n = int(input("Digite novamente: "))

a = 1
c = 1

for i in range(1, n + 1, 1):
    r = a + c
    print(r)
    a = r
    c += 2
    

