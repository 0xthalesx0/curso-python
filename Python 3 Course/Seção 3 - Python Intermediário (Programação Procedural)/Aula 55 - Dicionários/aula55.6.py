d1 = {
    1: 2,
    3: 4,
    5: 6,
}

d2 = {
    'a': 'b',
    'c': 'd',
}
d1.pop(5)  # Estoura (apaga) uma chave
d1.popitem()  # Estoura o ultimo item

d1.update(d2)  # Concatenou (+) os 2 dicionários
