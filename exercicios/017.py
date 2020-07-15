"""Tamanho da hipotenusa"""

# Calculo da hipotenusa 


import math  # 1º Contato com importação de bibliotecas 
co = int(input('Digite o cateto oposto: '))
ca = int(input('Digite o cateto adjacente: '))
calc_c1 = pow(c_o, 2)
calc_c2 = pow(c_a, 2)
hip = calc_c1 + calc_c2
# raiz_hip = math.sqrt(hip)
# print('A soma do CO = ({})² com o CA = ({})² é igual a hipotenusa = {}'.format(c_o, c_a, math.sqrt(hip)))
print('A soma do CO = ({})² com o CA = ({})² é igual a hipotenusa = {}'.format(c_o, c_a, math.hypot(c_o, c_a)))
