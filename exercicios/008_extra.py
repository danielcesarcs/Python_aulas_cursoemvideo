# Conversão das principais unidades de medida apartir do METRO
# Utilizando maior interação

metro = float(input('\033[32mDigite a medida em\033[m \033[32;4;1mMETROS\033[m \033[32mque deseja converter\033[m\nR = '))
print()
print('\033[31;4mPara qual unidade de medida deseja que seja feita a conversão\033[m;\n'
    '\033[31mPor favor digite uma dessas iniciais abaixo\033[m.\n'
    '\033[32mPara Quilômetros:\033[m     \033[36mkm\033[m\n'
    '\033[32mPara Centímetero:\033[m     \033[36mcm\033[m\n'
    '\033[32mPara Milímetro:\033[m       \033[36mmm\033[m\n'
    '\033[32mPara Milhas:\033[m          \033[36mmi\033[m\n'
    '\033[32mPara Jardas:\033[m          \033[36mjr\033[m\n'
    '\033[32mPara Pés:\033[m             \033[36mp\033[m\n'
    '\033[32mPara Polegadas:\033[m       \033[36mpl\033[m\n'
    '\033[32mPara Milhas Náuticas:\033[m \033[36mmn\033[m\n')
conversao = str(input('\033[31;4mDigite qual unidade de comprimento deseja que seja feita a conversão:\033[m '))
print()
if conversao == 'km':
    mkm = metro / 1000
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Km é igual\033[m \033[31m{} Km\033[m'.format(metro, mkm))
    print('\033[4;31mPara obter esse valor divida a metros / 1000\033[m')
elif conversao == 'cm':
    mcm = metro * 100
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Centimetros é igual a\033[m \033[31m{:.4f} Cm\033[m'.format(metro, mcm))
    print('\033[31;4mPara realizar a conversão multiplique metros * 100\033[m')
elif conversao == 'mm':
    mmm = metro * 1000
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Milímetros é igual a\033[m \033[31m{:.4f} Mm\033[m'.format(metro, mmm))
    print('\033[31;4mPara realizar a conversão multiplique metros * 1000\033[m')
elif conversao == 'mi':
    mmi = metro / 1609
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Milhas é igual a\033[m \033[31{:.4f} Mi\033[m'.format(metro, mmi))
    print('\033[31;4mPara realizar a conversão divida metros / 1609\033[m')
elif conversao == 'jr':
    mjr = metro * 1.094
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Jardas é igual a\033[m \033[31{:.4f} Jardas\033[m'.format(metro, mjr))
    print('\033[31;4mPara realizar a conversão multiplique metro * 1,094\033[m')
elif conversao == 'p':
    mp = metro * 3.281
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Pés é igual a\033[m \033[31{:.4f} Pés\033[m'.format(metro, mp))
    print('\033[31;4mPara realizar a conversão multiplique metro * 3,281\033[m')
elif conversao == 'pl':
    mpl = metro * 39.37
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Polegadas é igual a\033[m \033[31m{:.4f} Polegadas\033[m'.format(metro, mpl))
    print('\033[31;4mPara realizar a conversão multiplique metro * 39,37\033[m')
elif conversao == 'mn':
    mn = metro / 1852
    print('\033[32mO valor de\033[m \033[31m{} metros\033[m \033[32mem Milhas Náuticas é igual a\033[m \033[31m{:.4f} Milhas Náuticas\033[m'.format(metro, mn))
    print('\033[31;4mPara realizar a conversão divida metros / 1852\033[m')
print()
print('\033[31;1;4mFIM DA OPERAÇÃO...\033[m')

