"""
count - Itertools
"""
from itertools import count

contador = count()

lista = ['Luiz', 'João', 'Maria', 'José', 'Thales']

lista = zip(contador, lista)

print(dict(lista))

