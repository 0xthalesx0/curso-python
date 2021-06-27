from dados import produtos, pessoas, lista
from functools import reduce

soma_precos = reduce(lambda ac, p: p['preco'] + ac, produtos, 0)
print(soma_precos)
print(round((soma_precos / len(produtos)), 2))