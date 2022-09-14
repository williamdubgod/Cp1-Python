#Entrar via teclado com “N” valores quaisquer. O valor “N” (que representa a quantidade de números) será digitado, deverá ser positivo, mas menor que vinte. Caso a quantidade não satisfaça a restrição, enviar mensagem de erro e solicitar o valor novamente. Após a digitação dos “N” valores, exibir:
# a) O maior valor;
# b) O menor valor;
# c) A soma dos valores;
# d) A média aritmética dos valores;
# e) A porcentagem de valores que são positivos;
# f) A porcentagem de valores negativos;
# Use while.

s = 0
q = int(input("Digite a quantidade de números que serão digitados: "))

for i in range(1, q, 1):
    n = int(input("Digite um valor: "))
    while(n > 20):
        print("O número deve ser menor que 20!")
        n = int(input("Digite novamente um valor: "))

    if i == 1:
        maior = n
    elif n > maior:
        maior = n
    
    s = s + n

media = s / 10
print(f"O maior valor é o {maior}, a soma dos valores é {s}, e a média deles é {media}")
