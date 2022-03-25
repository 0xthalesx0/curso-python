perguntas = {
    'Pergunta 1': {
        'Pergunta': 'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '3',
            'c': '4'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 2': {
        'Pergunta': 'Quanto é 3*2?',
        'respostas': {
            'a': '4',
            'b': '10',
            'c': '6'
        },
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'Pergunta': 'Quanto é 5/5?',
        'respostas': {
            'a': '5',
            'b': '0',
            'c': '1'
        },
        'resposta_certa': 'c',
    },
}

pontuacao = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["Pergunta"]}')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Sua resposta: ")
    if resposta_usuario == pv['resposta_certa']:
        pontuacao += 1
    print()

print(f'Sua pontuação: {pontuacao}')