#Fazer um programa para receber um número e validar se esse número é positivo. Após isso, exibir a tabuada de 1 a 10 desse número. Use while

print('Tabuada com WHILE')
 
num = int(input("Digite um numero para obter a tabuada: "))
 
while(num <= 0):
    print("Não pode numero negativo!")
    num = int(input("Digite um outro numero para obter a tabuada: "))
 
i = 1
 
while(i < 11):
    r = num * i
    print(f'{num} X {i} = {r}')
    i = i + 1