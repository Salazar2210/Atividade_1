total_Leitura_pressao = float(input("Digite o número total de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
pressao_media = 0

while total_Leitura_pressao > 0:
    pressao = float(input("Digite a pressão atual que o duto sofre: "))
    if pressao >150:
        pressao_ajustada = pressao * 0.92
    else:
        pressao_ajustada = pressao * 0.96
    if 120<= pressao_ajustada <= 180:
        print("A pressão está na Zona Verde (Estável).")
    elif 180 < pressao_ajustada <= 250:
        print("A pressão está na Zona Amarela (Oscilação).")
    else:
        print("A pressão está na Zona Vermelha (Crítica).")
        
# pensar em uma forma de verificar se tem duas zonas vermelhas seguidas
    if cont_vermelho == 2:
        print("O sistema deve ser interrompido imediatamente por segurança.")
        total_Leitura_pressao = 0
    pressao_media += pressao

pressao_media = pressao_media / total_Leitura_pressao
