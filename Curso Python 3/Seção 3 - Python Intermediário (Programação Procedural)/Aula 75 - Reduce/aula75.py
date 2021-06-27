from dados import produtos, pessoas, lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)

soma_lista = reduce(lambda acumulador, item: item + acumulador, lista, 0)
print(soma_lista)