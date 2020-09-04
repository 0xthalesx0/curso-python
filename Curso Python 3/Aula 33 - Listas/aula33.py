#         0    1         2    3    4    5
lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
#   -     5    4    3    2    1


string = 'ABacanaCDE'

lista[5] = 'Qualquer outra coisa'
print(string[1])
print(lista[1])
print(lista[-1])
print(lista[:3])
print(lista[::2])
print(lista[::-1]) #exibe ao contrário

