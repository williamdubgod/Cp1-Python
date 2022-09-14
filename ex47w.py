# Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
# a) O maior valor;
# b) A soma dos valores;
# c) A média aritmética dos valores;
# Use While.

s = 0
i = 0
maior = 0

while i < 10:
    n = int(input("Digite um valor: "))
    while(n < 0):
        print("O número deve ser positivo!")
        n = int(input("Digite novamente um valor: "))

    if i == 1:
        maior = n
    elif n > maior:
        maior = n
    
    s = s + n
    i += 1
media = s / 10
print(f"O maior valor é o {maior}, a soma dos valores é {s}, e a média deles é {media}")