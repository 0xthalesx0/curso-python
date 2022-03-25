from dados import produtos, pessoas, lista


def filtra(produto):
    if produto['preco'] > 50:
        produto['caro'] = True
    return True

def filtra2(pessoa):
    return pessoa['idade'] >= 18

# VERSÃO MAP
# nova_lista = filter(lambda x: x > 5, lista)
# print(list(nova_lista))

# VERSÃO LIST COMPREHENSION
# nova_lista = [x for x in lista if x > 5]
# print(list(nova_lista))

#nova_lista = filter(lambda p: p['preco'] > 50, produtos)


nova_lista1 = filter(filtra, produtos)
nova_lista2 = filter(filtra2, pessoas)

for produto in nova_lista1:
    print(produto)

print('\n----------------\n')

for produto in nova_lista2:
    print(produto)
