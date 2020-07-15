"""APRESENTAÇÃO DE NOME COM FORMATAÇÕES"""

# Formatação de strings

nome = input('Digite seu nome: ').strip()  # Remove espaços
print('TODAS LETRAS MAIÚSCULAS: ', nome.upper())
print('TODAS LETRAS MINUSCULAS: ', nome.lower())
print('NÚMERO DE CARACTERES SEM ESPAÇO: ', len(nome) - nome.count(' '))  # "Calculo" usado para apresentar numero de caracteres sem espaço
print('A quantidade de letras de seu primeiro nome é: ', nome.find(' '))
nsep = nome.split()  # Apenas primeiro nome; Criação de um lista
print('Primeiro nome: ', nsep[0])  # Escolha do elemento da lista criada
print('Quantidade de letras do primeiro nome: ', len(nsep[0]))
