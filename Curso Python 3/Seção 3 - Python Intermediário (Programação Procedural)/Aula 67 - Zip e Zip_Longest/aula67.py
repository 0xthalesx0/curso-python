"""
Zip - Unindo Iteráveis
Zip_longest - Itertools -> Precisa ser importado dessa biblioteca

Zip une até terminar a menor lista (ou seja, no exemplo abaixo, o 3º elemento 'BA' da segunda lista)
Zip_longest é até a maior lista e preenche o resto com "None" ou com o que colocar no argumento 'fillvalue=<preenchimento>'
"""
from itertools import zip_longest


cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Itatiba']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(estados, cidades)
cidades_estados2 = zip_longest(estados, cidades, fillvalue='Estado desconhecido')

"""
jeito ruim
print(next(cidades_estados))
print(next(cidades_estados))
print(next(cidades_estados))
"""

""" Melhor
for valor in cidades_estados:
    print(valor)
Depois disso, o iterador já está no fim, e não mostra mais valores a partir daqui
"""
# Mostra o objeto zip, e não os valores
print(cidades_estados)

# Lista corretamente
print(list(cidades_estados))
print(list(cidades_estados2))
