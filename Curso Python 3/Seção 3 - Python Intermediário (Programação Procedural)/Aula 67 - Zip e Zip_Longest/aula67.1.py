"""
Zip - Unindo Iteráveis
Zip_longest - Itertools -> Precisa ser importado dessa biblioteca

Zip une até terminar a menor lista (ou seja, no exemplo abaixo, o 3º elemento 'BA' da segunda lista)
Zip_longest é até a maior lista e preenche o resto com "None" ou com o que colocar no argumento 'fillvalue=<preenchimento>'
"""
from itertools import zip_longest, count

indice = count()
cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Itatiba']
estados = ['SP', 'MG', 'BA']

cidades_estados = zip(  # Cuidado! Se usar zip_longest com um gerador (count), vai acontecer um loop infinito!!
    indice,
    estados,
    cidades,
)

for indice, estado, cidade in cidades_estados:
    print(indice, estado, cidade)

