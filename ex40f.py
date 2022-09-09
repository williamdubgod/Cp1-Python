# Exibir a tabuada dos valores de um a vinte, no intervalo de um a dez. Entre as tabuadas, solicitar que o usuário pressione uma tecla. Use for.

for t in range(1, 21, 1):
    pergunta = input("Deseja ver a próxima tabuada? ")
    if pergunta == "não" or pergunta == "Não" or pergunta == "nao" or pergunta == "Nao":
        print("Obrigado!")
        break
    else:
        for i in range(1, 11, 1):
            r = t * i
            print(f'{t} X {i} = {r}')




        
        
            
            
 
