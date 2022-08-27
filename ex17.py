#A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”.

v1 = float(input("Digite o primeiro numero: "));
v2 = float(input("Digite o segundo numero: "));
v3 = float(input("Digite o terceiro numero: "));

lado1 = v1 + v2
lado2 = v1 + v3
lado3 = v2 + v3

triangulo = False

if v1 > 0 and v2 > 0 and v3 > 0 and lado1 > v3 or lado2 > v2 or lado3 > v1:
    print("Esses valores formam um triangulo.");
    triangulo = True;
else:
    triangulo = False;
print("Esses valores não formam um triângulo.")








