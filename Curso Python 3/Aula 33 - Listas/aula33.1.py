l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1)
print(l2)

l3 = l1 + l2
print(l3)
l4 = [7, 8, 9]
l4.extend(l1)  # Adiciona os valores da lista 1 na lista 4
l4.append(5)  # Adiciona um valor
print(l4)

l5 = [10, 11, 12]
l5.insert(0, 'banana')  # Adiciona no indice inserido, jogando os outros pra direita
l5.pop()  # Remove o ultimo item da lista
print(l5)
