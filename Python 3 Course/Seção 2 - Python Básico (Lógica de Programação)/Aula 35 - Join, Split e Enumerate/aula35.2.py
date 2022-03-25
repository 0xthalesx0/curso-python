string = "O Brasil é o pais do futebol, o Brasil é penta."
lista = string.split(' ')

# Isso:
for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

# É a mesma coisa que isso:
lista = [
    [0, 'Luiz'],
    [1, 'João'],
    [2, 'Maria'],
]

for indice, nome in lista:
    print(indice, nome)

lista = ["Luiz", "João", "Maria"]

n1, n2, n3 = lista

print(n2)
