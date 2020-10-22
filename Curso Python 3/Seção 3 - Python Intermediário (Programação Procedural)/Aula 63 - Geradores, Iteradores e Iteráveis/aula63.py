ex1 = [0, 1, 2, 3, 4, 5]
ex2 = 100
ex3 = "String"

print(hasattr(ex1, '__iter__'))  # hasattr = "Has Attribute", __iter__ = "Iterable"; True se obj for iterável
print(hasattr(ex2, '__iter__'))
print(hasattr(ex3, '__iter__'))

lista = ex1
for v in lista:  # transforma a lista em um Iterador (63.1), joga 1 valor de cada vez em V
    print(v)
