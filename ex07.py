# digitar o valor de 5 produtos. Exibir o valor e o troco.

p1 = float(input("Digite o valor do primeiro produto: "))

p2 = float(input("Digite o valor do segundo produto: "))

p3 = float(input("Digite o valor do terceiro produto: "))

p4 = float(input("Digite o valor do quarto produto: "))

p5 = float(input("Digite o valor do quinto produto: "))

total = p1 + p2 + p3 + p4 + p5

print("O valor total dos produtos foi: ", total)

dinheiro = float(input("Digite a quantidade de dinheiro: "))

troco = round(dinheiro - total, 2)

print("Seu troco é: ", troco)