# Calcular e exibir a soma dos “N” primeiros valores da seqüência abaixo. O valor “N” será digitado, deverá ser positivo, mas menor que cinqüenta. Caso o valor não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. A sequencia 2, 5/8, 10/27, 17/64... Use while.

n = int(input("Digite um número positivo e memor que 100: "))

while n < 0 or n >= 50:
    print("O número deve ser positivo e menor que 50")
    n = int(input("Digite novamente: "))

a = 1
c = 1 
i = 1
j = 1
m = 0

while j <= n:
    b = a + 1
    a = b
    d = c * c * c
    e = b/d
    print("{}/{}".format(b,d))
    i += 2
    c += 1
    m += e
    j += 1
print("O resultado da soma: {}".format(m))
    


    
