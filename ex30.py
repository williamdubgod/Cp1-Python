#  Escreva um algoritmo que leia três valores inteiros e diferentes e mostre-os em ordem crescente.

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))

if v1 < v2 and v2 < v3:
    print(v1, v2, v3)
elif v1 < v2 and v1 < v3 and v3 < v2:
    print(v1, v3, v2)
elif v2 < v1 and v1 < v3:
    print(v2, v1, v3)
elif v2 < v1 and v2 < v3 and v3 < v1:
    print(v2, v3, v1)
elif v3 < v1 and v3 < v2 and v2 < v1:
    print(v3, v2, v1)
elif v3 < v1 and v3 < v2 and v1 < v2:
    print(v3, v1, v2)
else:
    print("Os três números devem ser diferentes.")
