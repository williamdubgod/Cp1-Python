# verificar se a media das notas das provas foram maior ou igual a 5. Em caso positivo exibir aprovado. Em caso negativo exibir reprovado.


nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if (media >= 5):
    print(f"Sua média foi {media: 2f} você foi aprovado!")
else:
    print(f"Sua média foi {media: 2f} você foi reprovado!")

