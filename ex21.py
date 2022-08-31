# Fazer um programa para entrar via teclado com os valores das notas (P1 e P2) e calcular a média. Exibir a situação final do aluno (“Aprovado ou Reprovado”), sabendo que a média de aprovação é igual a cinco.

p1 = float(input("Digite sua nota da p1: "))
p2 = float(input("Digite sua nota da p2: "))

media = (p1 + p2) / 3

if media >= 5:
    print(f"Parabéns, sua média foi: {media:.2f}, você está aprovado!")
else: 
    print(f"Sua média foi: {media:.2f}, você está reprovado.")