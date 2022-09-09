# Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço normal de etiqueta e a escolha da condição de pagamento.

valor = float(input("Digite o valor do produto: "))
pagamento = input("Digite a forma de pagamento, cartão ou dinheiro, parcelamos em até 2x sem juros!: ")

if pagamento == "dinheiro" or pagamento == "Dinheiro":
    total = valor - (valor * 0.1)
    print("O total foi de:",total)

elif pagamento == "cartão" or pagamento == "Cartão" or pagamento == "Cartao" or pagamento == "cartao":
    vezes = input("Em quantas vezes?  ")
    if vezes == "2x" or vezes == "duas" or vezes == "2" or vezes == "duas vezes":
        print("O total foi de ",valor)
    elif vezes == "nenhuma" or vezes == "Nenhuma" or vezes == "zero" or vezes == "0":
        total = valor - (valor * 0.15)
        print("O total foi de:", total)
    else:
        total = valor + (valor * 0.1)
        print("O total foi de:",total)
else:
    print("Forma de pagamento não identificada, por favor digite dinheiro ou cartão.")

