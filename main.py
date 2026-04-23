import os
import funcoes

os.system('cls')
print(f'''
{'=' * 70}
{'Sistema de Escoamento de Unidades de Carga':^67}
{'=' * 70}\n
''')

total_Leitura_pressao = int(input("Digite o número total de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
cont_leituras_realizadas = total_Leitura_pressao
pressao_total = 0
totalRealizado = 0
contador_vermelho = 0
contador_verde = 0
menor = 500
maior = 0


while cont_leituras_realizadas > 0:
    pressao = float(input("Digite a pressão atual que o duto sofre: "))

    pressao_ajustada = funcoes.ajusteTerm(pressao)
    pressao_total += pressao_ajustada
    situacao = funcoes.situaPres(pressao_ajustada)

    if pressao_ajustada > maior:
        maior = pressao_ajustada
    elif pressao_ajustada < menor:
        menor = pressao_ajustada

    totalRealizado += 1
    cont_leituras_realizadas -= 1

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

pressao_media = pressao_total / totalRealizado
print(f"A média das pressões ajustadas é {pressao_media:.2f} UPC.")

print(f"A maior pressão exibida é de {maior} UPC.")
if totalRealizado == 1:
    menor = pressao_ajustada
print(f"A menor pressão exibida é de {menor} UPC.")

percentualVerde = contador_verde / total_Leitura_pressao * 100
print(f"Percentual de leituras que ficaram na Zona Verde é de {percentualVerde:.2f}%.")

percentualRealizado = totalRealizado / total_Leitura_pressao * 100
print(f"O percentual de leituras realizadas foi de {percentualRealizado:.2f}%.")

estabilidade = funcoes.condicao_duto(percentualVerde)
print(f'Estabilidade da operação: {estabilidade}')

risco = funcoes.chance_travamento(percentualRealizado)
print(f'Chance de travamento: {risco}')