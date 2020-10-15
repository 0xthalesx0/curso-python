d1 = {
    'c1': 'valor',
    'c2': 'Outro valor',
    'c3': 'Tupla',
}

for k in d1:
    print(k)    # Printa as chaves

for v in d1.values():
    print(v)    # Printa os valores

for i in d1.items():
    print(i)    # Printa os items em tuplas (chave, valor)

for d in d1.items():
    print(d[0], d[1])   # Printa os itens separadamente

for k, v in d1.items():
    print(k, v)  # Printa os itens separadamente, com desempacotamento
