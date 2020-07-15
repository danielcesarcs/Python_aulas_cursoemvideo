"""Aluguel por KM e dia"""

# Uso de operadores aritmeticos

dia = float(input('Quantos dias passou com o carro: '))
km = float(input('Quantos Km você andou com o carro: '))
pdia = dia * 60  # Cobrança p/dia
pkm = km * 0.15  # cobrança po km
pfim = pdia + pkm  # Soma final 
print('Você passou {} dias com o carro e rodou\n'
      '{}Km com ele, o preço final a ser pago é de: R${}'.format(dia, km, pfim))
