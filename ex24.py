# Exibir o seguinte seletor de opções e em função de uma escolha, solicitar os dados necessários para o cálculo da respectiva área. Enviar mensagem de erro se o usuário escolher uma opção inexistente.

menu = input("Qual dessas formas você deseja calcular a área? Triângulo, quadrado, retângulo ou círculo? Para sair difite 'fim': ")

if menu == "triângulo" or menu == "Triângulo" or menu == "triangulo" or menu == "Triangulo":
    base = float(input("Digite a base do triângulo: "))
    altura = float(input("Digite a altura do triângulo: "))
    area = (base *  altura) / 2
    print("A área do seu triângulo é: ", area)

elif menu == "quadrado" or menu == "Quadrado":
    lado = float(input("Digite o lado do quadrado: "))
    area = lado * lado
    print("A área do seu quadrado é: ", area)
    
elif menu == "retângulo" or menu == "retangulo" or menu == "Retângulo" or menu == "Retangulo":
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    area = base * altura
    print("A área do seu retângulo é: ", area)

elif menu == "círculo" or menu == "circulo" or menu == "Círculo" or menu == "Circulo":
   raio = float(input("Digite o raio do círculo: "))
   area = 3.14 * (raio * raio)
   print("A área do seu círculo é de aproximadamente: ", area)

elif menu == "fim" or menu == "sair" or menu == "Sair" or menu == "Fim":
    print("Obrigado!")

else: 
    print("Opção inválida, escolha adição, subtração, multiplicação, divisão ou 'fim' se quiser sair.")

