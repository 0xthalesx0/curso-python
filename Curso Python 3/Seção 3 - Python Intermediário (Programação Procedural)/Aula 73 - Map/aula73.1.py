from dados import produtos, pessoas, lista


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


novos_produtos = map(aumenta_preco, produtos)

for preco in novos_produtos:
    print(preco)
