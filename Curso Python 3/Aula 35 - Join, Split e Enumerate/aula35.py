string = "O Brasil é o pais do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

print(lista1)
print(lista2)

for valor in lista1:
    print(valor)

palavra = ''
contagem = 0
for valor in lista1:
    print(f"A palavra {valor} apareceu {lista1.count(valor)}x na frase.")

    qtd = lista1.count(valor)
    if qtd > contagem:
        contagem = qtd
        palavra = valor

for valor in lista2:
    print(valor.strip().capitalize())  # Strip = Trim
