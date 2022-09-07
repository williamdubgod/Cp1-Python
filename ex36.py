#  Entrar via teclado com o sexo de determinado usuário, aceitar somente “F” ou “M” como respostas válidas.

sexo = input("Digite seu sexo (m) ou (f): ")

while ((sexo != "m") and (sexo != "f")):
    print("Por favor digite 'm' ou 'f'")
    sexo = input("Digite seu sexo: ")