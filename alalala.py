import os
import funcoes

os.system('cls')
total_Leitura_pressao = float(input("Digite o número total de leituras da pressão hidrodinâmica que serão realizadas no seu turno: "))
cont_leituras_realizadas = total_Leitura_pressao
pressao_total = 0
totalRealizado = 0
contador_vermelho = 0
contador_verde = 0
parar = 0
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
        print("⚠️  O sistema deve ser interrompido imediatamente por segurança ⚠️")
        break
    elif situacao == 'vd':
        contador_verde += 1
        contador_vermelho = 0
    elif situacao == 'a':
        contador_vermelho = 0
    else:
        contador_vermelho += 1
        if contador_vermelho == 2:
            print("⚠️  O sistema deve ser interrompido imediatamente por segurança ⚠️")
            break

print(f'''
\n{'=' * 35}
{' ' * 8}Resumo das leituras
{'=' * 35}
''')

pressao_media = pressao_total / total_Leitura_pressao
print(f"A média das pressões ajustadas é {pressao_media} UPC.")

print(f"A maior pressão exibida é de {maior} UPC.")
if totalRealizado == 1:
    menor = pressao_ajustada
print(f"A menor pressão exibida é de {menor} UPC.")

percentualVerde = contador_verde / total_Leitura_pressao * 100
print(f"Percentual de leituras que ficaram na Zona Verde é de {percentualVerde}%.")

percentualRealizado = totalRealizado / total_Leitura_pressao * 100
print(f"O percentual de leituras realizadas foi de {percentualRealizado}%.")