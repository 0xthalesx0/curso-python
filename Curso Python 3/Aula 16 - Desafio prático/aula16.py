nome = 'Luiz'
idade = 20
altura = 1.80
peso = 60
ano = 2020

ano_nasc = ano - idade
imc = peso/(altura**2)

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print('O imc de {} é {:.2f}'.format(nome, imc))
print(f'{nome} nasceu em {ano_nasc}')
