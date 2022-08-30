# Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos.

v1 = float(input("Digite o primeiro numero: "))
v2 = float(input("Digite o segundo numero: "))
v3 = float(input("Digite o terceiro numero: "))

if (v1 + v2) > v3 and (v1 + v3) > v2 and (v2 + v3) > v1:
    print("Esses valores formam um triângulo.")
    if ((v1 * v1) + (v2 * v2) == (v3 * v3)) or ((v1 * v1) + (v3 * v3) == (v2 * v2)) or ((v2 * v2) + (v3 * v3) == (v1 * v1)):
        print("Esse triângulo é retângulo.")
    else:
        print("Esse triângulo não é retângulo.")
else:
    print("Esses valores não formam um triângulo.")