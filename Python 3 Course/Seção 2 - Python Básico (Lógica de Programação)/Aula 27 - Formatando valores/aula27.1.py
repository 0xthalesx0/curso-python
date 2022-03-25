"""
Formatando valores

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TUPO - s, f ou d)

> - Esquerda
< - Direita
^ - Centro
"""

nome = 'Otávio'
sobrenome = 'Miranda'
nome_formatado = '{0:$^50} {1:#^50}'.format(nome, sobrenome)
print(nome_formatado)

print(nome.ljust(10, '#'))
print(nome.lower())  # Tudo minusculo
print(nome.upper())  # Tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas
