# Entrar via teclado com três valores distintos. Exibir o maior deles.


v1 = float(input("Digite o primeiro numero: "))
v2 = float(input("Digite o segundo numero: "))
v3 = float(input("Digite o terceiro numero: "))

maior = v1

if(v2 > maior):
    maior = v2
if(v3 > maior):
    maior = v3

print("O número maior é o: ", maior)
