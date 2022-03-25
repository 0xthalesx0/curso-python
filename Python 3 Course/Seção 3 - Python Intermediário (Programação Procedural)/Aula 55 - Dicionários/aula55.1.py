d1 = {
    'str': 'valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla',
}

print(d1[(1, 2, 3, 4)])

# print(d1[5]) isso daria erro
if 5 in d1:
    print(d1[5])

if d1.get('nomedachave') is not None:  # Se existir valor para o campo 'nomedachave'
    print(d1.get('nomedachave'))

print(123)

d1['nova_chave'] = 'novo valor'  # Mesma
d1.update({'nova_chave': 'novo valor'})  # Coisa

print('nova_chave' in d1)  # Mesma
print('nova_chave' in d1.keys())  # Coisa

print('novo valor' in d1.values())

print(len(d1))  # Chave: valor = 1 / Conta o # de pares
