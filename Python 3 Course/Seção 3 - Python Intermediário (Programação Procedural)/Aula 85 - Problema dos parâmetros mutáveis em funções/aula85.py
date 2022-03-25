def lista_cli(lista, cli=None):
    if cli is None:
        cli = []
    cli.extend(lista)
    return cli

ex = ['Fabricio']
clientes1 = lista_cli(['João', 'Maria', 'Eduardo'], ex)
clientes2 = lista_cli(['Marcos', 'Jonas', 'Zico'])

print(clientes1)
print(clientes2)