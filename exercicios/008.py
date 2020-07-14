"""metros para centimetros e milimetros"""

# Uso dos operadores aritméticos para conversão de unidades de medidas

metros = int(input('Digite a metragem: '))  # Uso da 'tipagem' para explicitação do valor recebido
mforcm = metros * 100
mformm = metros * 1000
print('Você digitou {} metros\nconvertido para cm fica: {}\ne para mm fica: {}'.format(metros, mforcm, mformm))
