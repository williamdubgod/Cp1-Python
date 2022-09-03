#Entrar via teclado com dois valores quaisquer. Após a digitação, exibir um seletor de opções (“menu”) com as seguintes opções: (Fazer esse exercício utilizando If..Else e/ou Case)

v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))

menu = input("Que operação você deseja fazer? Multiplicação, divisão, adição ou subtração? Caso deseje sair, digite 'fim': ")

if menu == "multiplicação" or menu == "Multiplicação" or menu == "multiplicacao" or menu == "Multiplicacao":
    print(v1 * v2)

elif menu == "adição" or menu == "Adição" or menu == "adicao" or menu == "Adicao" or menu == "soma" or menu == "Soma":
    print(v1 + v2)

elif menu == "subtração" or menu == "Subtração" or menu == "subtracao" or menu == "Subtracao":
    print(v1 - v2)

elif menu == "divisão" or menu == "Divisão" or menu == "divisao" or menu == "Divisao":
    print(v1 / v2)

elif menu == "fim" or menu == "Fim" or menu == "sair" or menu == "Sair":
    print("Obrigado!")

else:
    print("Opção inválida, escolha adição, subtração, multiplicação, divisão ou fim se quiser sair")








