# Entrar com o peso, o sexo e a altura de uma determinada pessoa. Após a digitação, exibir se esta pessoa está ou não com seu peso ideal. Fórmula: peso/altura².

altura = float(input("Digite a altura em (m): "))

peso = float(input("Digite o peso em (kg): "))

sexo = input("Digite seu sexo: ")

imc = peso / (altura * altura)

if (sexo == "feminino" or sexo == "Feminino" or sexo == "F" or sexo == "f"):
    if imc < 19:
        print("Abaixo do peso.")
    elif imc < 24:
        print("Peso ideal!")
    else:
        print("Acima do peso.")
else: 
    print("Sexo inválido, digite masculino (m) ou feminino (f)")

if (sexo == "masculino" or sexo == "Masculino" or sexo == "m" or sexo == "M"):
    if imc < 20:
        print("Abaixo do peso.")
    elif imc < 25:
        print("Peso ideal!")
    else: 
        print("Acima do peso.")