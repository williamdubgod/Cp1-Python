#Fazer um programa para receber um número e validar se esse número é positivo. Após isso, exibir a tabuada de 1 a 10 desse número. Use for.

print('Tabuada com FOR')
 
num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
for i in range(1, 11, 2):
    r = num * i
    print(f'{num} X {i} = {r}')