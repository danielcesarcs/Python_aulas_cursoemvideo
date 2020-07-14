# Conversão das principais unidades de medida apartir do METRO
# Utilizando maior interação

metro = float(input('Digite a medida em \033[32;4;1mMETROS\033[m que deseja converter: '))
print()
print('Para qual unidade de medida deseja que seja feita a conversão: \n'
    'Por favor digite uma dessas iniciais abaixo.'
    'Para Quilômetros: km\n'
    'Para Centímetero: cm\n'
    'Para Milímetro: mm\n'
    'Para Milhas: mi\n'
    'Para Jardas: jr\n'
    'Para Pés: p\n'
    'Para Polegadas: pl\n'
    'Para Milhas Náuticas: mn\n')
conversao = str(input('Digite qual unidade de comprimento deseja que seja feita a conversão: '))
print()
if conversao == 'km':
    mkm = metro / 1000
    print('O valor de {} metros em Km é igual {} Km'.format(metro, mkm))
    print('Para obter esse valor divida a metros / 1000')
elif conversao == 'cm':
    mcm = metro * 100
    print('O valor de {} metros em Centimetros é igual a {} Cm'.format(metro, mcm))
    print('Para realizar a conversão multiplique metros * 100')
elif conversao == 'mm':
    mmm = metro * 1000
    print('O valor de {} metros em Milímetros é igual a {} Mm'.format(metro, mmm))
    print('Para realizar a conversão multiplique metros * 1000')
elif conversao == 'mi':
    mmi = metro / 1609
    print('O valor de {} metros em Milhas é igual a {} Mi'.format(metro, mmi))
    print('Para realizar a conversão divida metros / 1609')
elif convers:
    pass

