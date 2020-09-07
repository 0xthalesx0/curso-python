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


num1 = 10
num2 = 3
divisao = num1 / num2
print('{:.2f}'.format(divisao))
print(f"{divisao:2f}")

nome = "Thales Daniel"
print(f'{nome:s}')  # só diz que isso é uma string

num3 = 10
print(f'{num3:a>10}')  # O valor que está ali terá CARACTERE numero de caracteres adicionados a >, < ou ^ da variável
print(f'{num3:b<10}')
print(f'{num3:c^10}')

nome2 = "Otavio Miranda"
print((50-len(nome2)) / 2)
print(f"{nome2:#^50}")