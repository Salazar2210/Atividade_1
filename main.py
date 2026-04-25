import os
import funcoes

os.system('cls')
print(f'''
================================================================================
                            REFINARIA DELTA-9
================================================================================
                                 SEUC-4: 
 Sistema de Escoamento de Unidades de Carga Duto Principal de Escoamento (DPE)
________________________________________________________________________________
      
 Unidade de medida : UPC
 Ajuste termico    : > 150 UPC = + 8% | <=150 UPC = - 4%
 Protocolo         : Travamento em 2x Zona Vermelha | 
________________________________________________________________________________
      
 ZONA VERDE    : 120 a 180 UPC  (ESTAVEL)
 ZONA AMARELA  : abaixo de 250  (OSCILACAO)
 ZONA VERMELHA : acima de 250   (CRITICA)
================================================================================\n''')

total_Leitura_pressao = int(input("Digite o número total de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
cont_leituras_realizadas = 1
pressao_anterior = 0
pressao_total_ajustada = 0
pressao_total_bruta = 0
totalRealizado = 0
contador_vermelho = 0
contador_verde = 0
menor = 500
maior = 0

os.system('cls')
while cont_leituras_realizadas != (total_Leitura_pressao + 1):
    pressao = float(input("\nDigite a pressão atual que o duto sofre: "))

    pressao_total_bruta += pressao
    pressao_ajustada = funcoes.ajusteTerm(pressao)
    pressao_total_ajustada += pressao_ajustada
    situacao = funcoes.situaPres(pressao_ajustada)
    funcoes.calcular_variacao_press(pressao_ajustada, pressao_anterior, cont_leituras_realizadas)

    if pressao_ajustada > maior:
        maior = pressao_ajustada
    if pressao_ajustada < menor:
        menor = pressao_ajustada
    
    if cont_leituras_realizadas > 0:
        pressao_anterior = pressao_ajustada
    
    totalRealizado += 1
    cont_leituras_realizadas += 1

    if situacao == 'c':
        print("\n⚠️   O sistema deve ser interrompido imediatamente por segurança ⚠️")
        break
    elif situacao == 'vd':
        contador_verde += 1
        contador_vermelho = 0
    elif situacao == 'a':
        contador_vermelho = 0
    else:
        contador_vermelho += 1
        if contador_vermelho == 2:
            print("\n ⚠️   O sistema deve ser interrompido imediatamente por segurança ⚠️")
            break

print(f'''
\n{'=' * 40}
{'Resumo das leituras':^40}
{'=' * 40}
''')

pressao_media_ajustada = pressao_total_ajustada / totalRealizado
pressao_media_bruta = pressao_total_bruta / totalRealizado
percentualVerde = contador_verde / totalRealizado * 100
percentualRealizado = totalRealizado / total_Leitura_pressao * 100
estabilidade = funcoes.condicao_duto(percentualVerde)
risco = funcoes.chance_travamento(percentualRealizado)

print(f'''
Média da pressão ajustada : {pressao_media_ajustada:.2f} UPC.
Média da pressão bruta    : {pressao_media_bruta:.2f} UPC.
Maior pressão medida      : {maior} UPC.
Menor pressão medida      : {menor} UPC.
Leituras na zona verde    : {percentualVerde:.2f}%.
Leituras realizadas foi   : {percentualRealizado:.2f}%.
Estabilidade da operação  : {estabilidade}
Chance de travamento      : {risco}
''')



