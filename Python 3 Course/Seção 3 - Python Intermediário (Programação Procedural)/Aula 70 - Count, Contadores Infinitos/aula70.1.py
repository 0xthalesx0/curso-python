"""
count - Itertools
"""
from itertools import count

contador = count()

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))
print("\n------------------------------------------------\n")

contador = count(start=5, step=0.1)
for valor in contador:  # retorna infinito!
    print(round(valor, 2))

    if valor>= 10:
        break  # Impede de retornar infinito!
