def ajusteTerm(pres):
    pressao_ajustada = pres * 1.08 if pres > 150 else pres * 0.96
    return pressao_ajustada

def situaPres(pres):
    if pres < 120:
        print('Fluído está cristalizado')
        situacao = 'c'
    elif pres < 180:
        print("🟢  A pressão está na Zona Verde (Estável). 🟢\n")
        situacao = 'vd'
    elif pres < 250:
        print("🟡  A pressão está na Zona Amarela (Oscilação). 🟡\n")
        situacao = 'a'
    else:
        print("🔴  A pressão está na Zona Vermelha (Crítica). 🔴\n")
        situacao = 'vm'
    return situacao

def condicao_duto(pct_verde):
    if pct_verde > 85:
        estado = 'Excelente - Operação predominantemente estável'
    elif pct_verde > 65:
        estado = 'Boa - Maioria das leituras estão estáveis'
    elif pct_verde > 40:
        estado = 'Regular - Atenção recomendada durante a operação do duto'
    else:
        estado = '⚠️  Crítica - O duto necessita de manutenção imediata ⚠️'
    return estado

def chance_travamento(pct_realizado):
    if pct_realizado < 50:
        estado = '⚠️ Alto Risco de travamento durante o próximo turno ⚠️'
    elif pct_realizado < 70:
        estado = 'Risco moderado de travamento durante o próximo turno'
    elif pct_realizado < 90:
        estado = 'Baixo risco de travamento durante o próximo turno'
    else:
        estado = 'Chance mínimas de ocorrer um travamento'
    return estado

def calcular_variacao_press(press_atual, press_ant, cont_leit):
    if cont_leit > 1:
        variacao = press_atual - press_ant
        direcao = 'subiu' if variacao > 0 else 'abaixou'
        print(f'A pressão {direcao} em {abs(variacao):.2f} UPC')