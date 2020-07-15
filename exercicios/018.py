"""Sen, Cos e Tg de um ângulo"""

# Seno, Cosseno e Tangente de um ângulo
# Sem uso dos metodos especificos, apenas com operadores

"""
import math
c_o = int(input('Digite o cateto oposto do triangulo: '))
c_a = int(input('Digite o cateto adjacente do triangulo: '))
hip = (pow(c_o, 2) + pow(c_a, 2))
print('A soma do CO({})² com o CA({})² é igual a hipotenusa {}'.format(c_o, c_a, math.sqrt(hip)))
print()
print('O valor do Seno é igual a: {}'.format(c_o / math.sqrt(hip)))
print()
print('O valor do Cosseno é igual a: {}'.format(c_a / math.sqrt(hip)))
print()
print('O valor da Tangente é igual a: {}'.format(c_o / c_a))
print()
print('FIM DA OPERAÇÃO')
"""

# Uso dos metodos especificos para calculo de ângulo

import math
angulo = float(input('Digite o grau dos catetos: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O valor do seno: {:.2f}\n'
      'O valor do cosseno: {:.2f}\n'
      'O valor da Tangente: {:.2f}'.format(seno, cos, tan))
