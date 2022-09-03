# Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que C.

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

ab = a + b

if ab > c:
    print(ab, "é maior que",c, "logo a + b é maior que c")

elif ab == c:
    print(ab, "é igual a",c, "logo a + b é idêntico a c")

else:
    print(ab, "não é menor que",c, "logo a + b é menor que c")
