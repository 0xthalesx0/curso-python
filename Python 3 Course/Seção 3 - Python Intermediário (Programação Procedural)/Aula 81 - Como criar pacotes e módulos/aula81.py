from vendas.calc_preço import aumento, reducao

preco = 50

preco_aum = aumento(preco, 15, True)
print(preco_aum)

preco_red = reducao(preco, 15, True)
print(preco_red)