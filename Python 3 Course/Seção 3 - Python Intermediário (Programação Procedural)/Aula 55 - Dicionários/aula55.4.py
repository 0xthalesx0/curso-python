# import copy  # Esse método realmente copia o dicionário

d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ['Luiz', 'Otávio']}
v = d1  # ISSO AQUI NÃO CRIA OUTRO DICT, ELE É UM PONTEIRO
w = d1.copy()  # ISSO AQUI COPIA O DICT (SHALLOW COPY)
# x = copy.deepcopy(d1)  # ISSO AQUI COPIA TUDO (DEEP COPY)

w[1] = 'Luiz'

print(v['d'][0])  # Acessa o valor 0 de D
v['d'][0] = 'João'  # Como é uma shallow copy, ele não altera 'd', mas altera 'd'[0]

print(d1)
print(v)
