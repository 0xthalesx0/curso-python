from random import randint

valores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]


def valida_cnpj(cnpj):
    cnpj_dig1 = str(cnpj) + str(calc_dig(cnpj, 1))
    cnpj_dig2 = str(cnpj_dig1) + str(calc_dig(cnpj_dig1, 2))
    cnpj_final = tratar_cnpj(cnpj_dig2)
    return cnpj_final

def tratar_cnpj(cnpj):
    if len(cnpj) == 18:
        cnpj = cnpj.replace('.', '')
        cnpj = cnpj.replace('/', '')

        return cnpj[:-3]
    elif len(cnpj) == 14:
        cnpj = cnpj[:2] + '.' + cnpj[2:5] + '.' + cnpj[5:8] + '/' + cnpj[8:12] + '-' + cnpj[12:]
        return cnpj
    else:
        print('algo errado')


def calc_dig(cnpj, dig):
     if dig == 1:
         lista = valores[1:]
     elif dig == 2:
         lista = valores
     else:
         print('Erro')
     soma = 0
     i = 0
     for digito in cnpj:
         soma = soma + (int(digito) * lista[i])
         i = i+1

     digito = 11 - (soma % 11)
     return digito if digito <= 9 else 0

print("CNPJ Gerados:")
for i in range(5):
    print(valida_cnpj(str(randint(100000000000, 999999999999))))

