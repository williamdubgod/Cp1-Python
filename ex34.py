#  Criar uma rotina de entrada que aceite somente um valor positivo.

num = int(input("Digite um número positivo: "))

while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero: "))