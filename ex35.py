# Entrar com dois valores via teclado, onde o segundo deverá ser maior que o primeiro. Caso contrário solicitar novamente apenas o segundo valor.

v1 = float(input("Digite um número: "))
v2 = float(input("Digite um número maior que o primeiro: "))

while (v1 > v2):
    print("O valor deve ser maior que o primeiro!")
    v2 = float(input("Digite outro valor: "))