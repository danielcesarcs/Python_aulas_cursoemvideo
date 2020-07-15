"""Ordem dos Sorteados"""

# Uso da importação de bibliotecas

import random
a = input('Aluno 1: ')
b = input('Aluno 2: ')
c = input('Aluno 3: ')
d = input('Aluno 4: ')
lista = [a, b, c, d]
random.shuffle(lista)  # Metodo vai embaralhar a lista e reorganizar
print('A ordem de sortedos é: ')
print(lista)
