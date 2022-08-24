altura = float(input("Digite sua altura em (m): "));

peso = float(input("Digite seu peso em (kg): "));

imc = peso / (altura * altura)

if (imc < 20):
    print("Abaixo do peso!");
elif imc < 25: 
    print("Peso ideal!");
else: 
    print("Acima do peso!");

    
