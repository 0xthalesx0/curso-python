from dados import produtos, pessoas, lista

def aumenta_idade(p):
    p['nova_idade'] = round(p['idade'] * 1.2)
    return p


nomes = map(lambda p: p['nome'], pessoas)
idades = map(lambda p: p['idade'], pessoas)

for pessoa in nomes:
    print(pessoa)

print()

for idade in idades:
    print(idade)

print()

nomes = map(aumenta_idade, pessoas)
for pessoa in nomes:
    print(pessoa)