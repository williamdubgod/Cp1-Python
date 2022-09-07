#  Entrar via teclado com um valor (X) qualquer. Travar a digitação, no sentido de aceitar somente valores positivos. Solicitar o intervalo que o programa que deverá calcular a tabuada do valor digitado, sendo que o segundo valor (B), deverá ser maior que o primeiro (A), caso contrário, digitar novamente somente o segundo. Após a validação dos dados, exibir a tabuada do valor digitado, no intervalo decrescente, ou seja, a tabuada de X no intervalo de B para A. Use for.

num = int(input("Digite um numero para obter a tabuada: "))
a = int(input("Digite o intervalo inicial da tabuada: "))
b = int(input("Digite o intervalo final da tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
while (b < a):
    print("O intervalo final deve ser maior que o inicial.")
    b = int(input("Digite novamente o intervalo final: "))

for i in range(b, a - 1, -1):
    r = num * i
    print(f'{num} X {i} = {r}')

