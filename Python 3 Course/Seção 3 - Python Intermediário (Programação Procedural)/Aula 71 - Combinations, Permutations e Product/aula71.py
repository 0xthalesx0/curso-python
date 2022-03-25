"""
Combinations, Permutations e Product - itertools
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations

pessoas = ['Luiz', 'André', 'Eduardo', 'Letícia', 'Fabrício', 'Rose']

for grupo in combinations(pessoas, 3):  # combinações de 2 pessoas do grupo iteradas
    print(grupo)

print("\n-----\n")

for grupo in permutations(pessoas, 2):  # combinações de 2 pessoas do grupo iteradas
    print(grupo)
