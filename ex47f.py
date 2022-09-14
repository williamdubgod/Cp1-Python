# Entrar via teclado com dez valores positivos. Consistir a digitação e enviar mensagem de erro, se necessário. Após a digitação, exibir:
# a) O maior valor;
# b) A soma dos valores;
# c) A média aritmética dos valores;
# Use for.

s = 0

for i in range(1, 11, 1):
    n = int(input("Digite um valor: "))
    while(n < 0):
        print("O número deve ser positivo!")
        n = int(input("Digite novamente um valor: "))

    if i == 1:
        maior = n
    elif n > maior:
        maior = n
    
    s = s + n

media = s / 10
print(f"O maior valor é o {maior}, a soma dos valores é {s}, e a média deles é {media}")