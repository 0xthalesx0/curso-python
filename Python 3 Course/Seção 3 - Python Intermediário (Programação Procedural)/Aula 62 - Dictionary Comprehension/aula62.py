lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2'),
]

d1 = {x: y for x, y in lista}  # Idêntico à linha abaixo, mas você pode alterar com .funções, invertendo variaveis, etc.
# d2 = dict(lista)

d2 = {x for x in range(5)}  # ISTO É UM SET, NÃO UM DICT

d3 = {f'chave_{x}': x**2 for x in range(5)}

print(d1, type(d1))
print(d2, type(d2))
print(d3, type(d3))
