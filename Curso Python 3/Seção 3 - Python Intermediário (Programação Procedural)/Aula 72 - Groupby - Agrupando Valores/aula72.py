from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'C'},
    {'nome': 'Rosemary', 'nota': 'A'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'C'},
    {'nome': 'Anderson', 'nota': 'A'},
    {'nome': 'José', 'nota': 'D'},
    {'nome': 'Maria', 'nota': 'B'},
]

ordena = lambda item: item['nota']
alunos.sort(key=ordena)  # SEM ORDENAÇÃO O GROUPBY NÃO FUNCIONA! FICA BUGADO!

for aluno in alunos:
    print(aluno)

print("\n---------------------------------------------------------------------------------")

alunos_agrupados = groupby(alunos, ordena)

for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)  # COPIA VALORES ITERÁVEIS PARA OS 2 VALORES, PRA QUE NÃO SE ESGOTE OS VALORES DOS ITERÁVEIS
    print(f'\nAgrupamento: {agrupamento}')

    quantidade = len(list(va2))  # ISSO ESGOTA O ITERÁVEL, QUALQUER FOR EMBAIXO NÃO VAI LER. TEE COPIA OS ITERADORES
    print(f'{quantidade} alunos tiraram a nota {agrupamento}:')

    for aluno in va1:
        print(f'\t{aluno}')

