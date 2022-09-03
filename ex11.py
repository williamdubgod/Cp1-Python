#Entrar via teclado, com dois valores distintos. Exibir o menor deles.

v1 = float(input("Digite o primeiro numero: "))
v2 = float(input("Digite o segundo numero: "))

if v1 < v2:
    print(v1, "É menor que", v2)
else: 
    print(v2, "É menor que", v1)