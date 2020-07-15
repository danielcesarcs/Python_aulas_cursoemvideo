"""Sorteio"""

# Uso da biblioteca random
# 1º contato com lista - sem aprofundamento
import random
a = input('Aluno 01: ')
b = input('Aluno 02: ')
c = input('Aluno 03: ')
d = input('Aluno 04: ')
lista = [a, b, c, d]
sor = random.choice(lista)  # 1 escolha na lista
print('O sorteado foi: {}'.format(sor))
