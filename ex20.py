# A partir dos valores da aceleração (a em m/s2), da velocidade inicial (v0 em m/s) e do tempo de percurso (t em s). Calcular e exibir a velocidade final de automóvel em km/h. 

vInicial = int(input("Digite a velocidade inicial em (m/s²): "))
aceleracao = int(input("Difite a aceleração em (m/s²): "))
tempo = int(input("Digite o tempo do percurso, em segundos: "))

velocidade = vInicial + (aceleracao * tempo)

print("Velocidade final: ", velocidade)

if velocidade > 120:
    print("Veículo muito rápido!")
elif velocidade > 80 and velocidade <= 120:
    print("Veículo rápido.")
elif velocidade > 60 and velocidade <= 80:
    print("Velocidade de cruzeiro.")
elif velocidade > 40 and velocidade <= 60:
    print("Velocidade permitida.")
else: 
    print("Veículo lento.")

