lista = [0, 1, 2, 3, 4, 5]
print("Lista é um iterador" if hasattr(lista, "__next__") else "Lista não é um iterador")
# Verifica se a lista possui o atr next, ou seja, se ela é um iterador
print(lista)

lista = iter(lista)  # Transforma a lista num iterador
print("Lista é um iterador" if hasattr(lista, "__next__") else "Lista não é um iterador")
print(lista)  # Mostra onde está o iterador na memória, use next(lista) pra começar a printar (next = lista[0])


print(next(lista))  # lista[0]
print(next(lista))  # lista[1]
print(next(lista))  # lista[2]
print(next(lista))  # lista[3]
print(next(lista))  # lista[4]
print(next(lista))  # lista[5]
print(lista)
