total_Leitura_pressao = float(input("Digite o número total de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
pressao_media = 0
totalRealizado = 0
cont_vermelho = 0
cont_verde = 0
ant = None
atual = None
menor = 500
maior = 0

while total_Leitura_pressao > 0:
    pressao = float(input("Digite a pressão atual que o duto sofre: "))

    if pressao >150:
        pressao_ajustada = pressao * 1.08
    else:
        pressao_ajustada = pressao * 0.96

    if 120<= pressao_ajustada <= 180:
        print("A pressão está na Zona Verde (Estável).")
        atual = 'verde'
        cont_vermelho = 0
        cont_verde += 1
        pressao_media += pressao_ajustada

    elif 180 < pressao_ajustada <= 250:
        print("A pressão está na Zona Amarela (Oscilação).")
        atual = 'amarelo'
        cont_vermelho = 0
        pressao_media += pressao_ajustada
    else:
        print("A pressão está na Zona Vermelha (Crítica).")
        atual = 'vermelho'
        cont_vermelho += 1
        pressao_media += pressao_ajustada
    ant = atual 
    
    if cont_vermelho == 2:
        print("O sistema deve ser interrompido imediatamente por segurança.")
        total_Leitura_pressao = 0

    if pressao_ajustada > maior:
        maior = pressao_ajustada
    elif pressao_ajustada < menor:
        menor = pressao_ajustada

    totalRealizado += 1
    total_Leitura_pressao -= 1
    
pressao_media = pressao_media / total_Leitura_pressao
print(f"A média das pressões ajustadas é {pressao_media}.")

print(f"A menor pressão exibida é de {menor}UPC.")

percentualVerde = cont_verde / total_Leitura_pressao * 100
print(f"Percentual de leituras que ficaram na Zona Verde é de {percentualVerde}%.")

percentualRealizado = totalRealizado / total_Leitura_pressao * 100
print(f"O percentual de leituras realizadas foi de {percentualRealizado}%.")