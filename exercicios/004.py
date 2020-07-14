"""Tipagem de dados"""

# Classificação de dados

v1 = input('Digite algo: ')
print(f'Tipo primitivo: {type(v1)}\nTem letras e números: {v1.isalnum()}\nTem letras: {v1.isalpha()}\n'
      f'Tem digitos: {v1.isdigit()}\nSe é números: {v1.isnumeric()}\nPode aparecer na tela: {v1.isprintable()}\n'
      f'Tem espaços: {v1.isspace()}\nEstá DEScaptalizado: {v1.istitle()}')

