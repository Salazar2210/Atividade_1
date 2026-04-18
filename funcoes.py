def ajusteTerm (pres):
    if pres > 150:
        pressao_ajustada = pres * 1.08
    else:
        pressao_ajustada = pres * 0.96
    return pressao_ajustada

def situaPres (pres):
    if pres < 120:
        print('Fluído está cristalizado')
        situacao = 'c'
        return situacao
    
    if pres < 180:
        print("A pressão está na Zona Verde (Estável).")
        situacao = 'vd'
        return situacao

    elif pres < 250:
        print("A pressão está na Zona Amarela (Oscilação).")
        situacao = 'a'
        return situacao
    
    else:
        print("A pressão está na Zona Vermelha (Crítica).")
        situacao = 'vm'
        return situacao
