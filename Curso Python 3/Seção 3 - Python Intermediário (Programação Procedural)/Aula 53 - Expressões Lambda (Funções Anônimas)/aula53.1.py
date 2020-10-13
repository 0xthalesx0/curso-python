lista = [
    ['P1', 13],
    ['P2', 10],
    ['P3', 1],
    ['P4', 3],
    ['P5', 15],
]


def func(item):
    return item[1]


# print(sorted(lista, key=func))
print(sorted(lista, key=lambda item: item[1]))  # Isso não edita a lista
print(lista)

# lista.sort(key=func)
lista.sort(key=lambda item: item[1])  # Isso edita a lista
print(lista)


