#Calcular e exibir a área de um retângulo, a partir dos valores da base e altura que serão digitados. Se a área for maior que 100, exibir a mensagem “Terreno grande”.

base = float(input("Digite o valor da base do terreno em (m): "))

altura = float(input("Digite o valor da altura do terreno em (m): "))

area = base * altura

print(f"A área do terreno é de: {area}m")

if area > 100:
    print("Seu terreno é grande.")
