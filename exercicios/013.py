"""Aumento salário"""

# Calculo de aumento de salário

s_i = float(input('Digite o salário: '))
aumen = (s_i * 15) / 100
s_f = s_i + aumen
print('O seu salário era: R${}, parabéns você recebeu\n'
      'aumento de 15% ({:.2f}) e agora seu salário é de: R${:.2f}'.format(s_i, aumen, s_f))  # 1º contato com formatação
