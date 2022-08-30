#A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”.

v1 = float(input("Digite o primeiro numero: "))
v2 = float(input("Digite o segundo numero: "))
v3 = float(input("Digite o terceiro numero: "))

if (v1 + v2) > v3 and (v1 + v3) > v2 and (v2 + v3) > v1:
    print("Esses valores formam um triângulo.")
    if v1 == v2 and v2 == v3:
        print("Esse triângulo é equilátero.")
    if (v1 == v2 and v1 != v3) or (v3 == v2 and v3 != v1) or (v1 == v3 and v1 != v2):
        print("Esse é um triângulo isósceles.")
    if (v1 != v2 and v2 != v3 and v1 != v3):
        print("Esse é um triângulo escaleno.")
else: 
    print("Esses valores não formam um triângulo.")
    