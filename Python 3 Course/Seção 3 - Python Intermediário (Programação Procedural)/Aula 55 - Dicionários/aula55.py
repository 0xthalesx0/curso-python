d1 = {'chave1': 'valor da chave 1'}
print(d1)

d1['chave2'] = 'valor da chave 2'
print(d1)

print(d1['chave1'])

#############################

d2 = dict(chave1='valor da chave 1', chave2='valor da chave 2')  # Mesma coisa

d3 = {'chave': 1, 'chave': 2, 'chave': 3}  # Isso aqui apenas atualiza o valor da chave que já foi criada pro ultimo
print(d3)  # Mostra "{'chave' : 3}"
