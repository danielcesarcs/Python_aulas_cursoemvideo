"""Compra de doláres"""

# Conversão obtida atraves de um valor ficticio

cai = float(input('Quantos reais você tem: '))
compra = cai / 3.27
print('Você tem R$ {} na carteira;\n'
      'em conversão aproximada (Levando em conta U$1,00 = R$3,27)\n'
      'você terá U$ {:.2f} caso realize a compra.'.format(cai, compra))
