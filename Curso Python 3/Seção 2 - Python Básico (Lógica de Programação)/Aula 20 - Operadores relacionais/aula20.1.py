nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')

idade = int(idade)

idade_menor = 18
idade_maior = 30


if idade_menor <= idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo.')
else:
    print(f'{nome} NÃO pode pegar o empréstimo.')
