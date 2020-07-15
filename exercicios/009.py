"""Tabuada de um inteiro"""

# Uso dos operadores aritméticos

num = int(input('Digite um número: '))
inicio = 'Resultado'
fim = 'Fim'
print()
print('{:=^25}'.format(inicio))
print()
print(f'{num} x 0 = {num*0}\n'
      f'{num} x 1 = {num*1}\n'
      f'{num} x 2 = {num*2}\n'
      f'{num} x 3 = {num*3}\n'
      f'{num} x 4 = {num*4}\n'
      f'{num} x 5 = {num*5}\n'  
      f'{num} x 6 = {num*6}\n'
      f'{num} x 7 = {num*7}\n'
      f'{num} x 8 = {num*8}\n'
      f'{num} x 9 = {num*9}\n'
      f'{num} x 10 = {num*10}')
print()
print('{:=^25}'.format(fim))
