#  Faça um algoritmo que leia o nome, o sexo e o estado civil de uma pessoa. Caso sexo seja “F” e estado civil seja “CASADA”, solicitar o tempo de casada (anos).

nome = input("Digite seu nome: ")
sexo = input("Digite seu sexo: ")
estadoCivil = input("Digite seu estado civil: ")

if (sexo == "F" or sexo == "f" or sexo == "feminino" or sexo == "Feminino") and (estadoCivil == "Casada" or estadoCivil == "casada"):
    tempo = input("Há quanto tempo você é casada? ")
    print("Obrigado pelos dados!")
