lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista
print(n1, n2)

lista2 = ['a', 'b', 'c', 'd', 'e']
a1, a2, *restante, aUltimo = lista2

print(restante)
print(a1, a2, aUltimo)

lista3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

*_, nAntepenultimo, nPenultimo, nUltimo = lista3  # *_ significa para outros devs que você não está utilizando o restante da lista
print(_)
