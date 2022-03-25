valores = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

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


cnpj = input('Digite o CNPJ a ser validado: ')

cnpj_tratado = tratar_cnpj(cnpj)

cnpj_dig1 = str(cnpj_tratado) + str(calc_dig(cnpj_tratado, 1))

cnpj_dig2 = str(cnpj_dig1) + str(calc_dig(cnpj_dig1, 2))

cnpj_final = tratar_cnpj(cnpj_dig2)

print('CNPJ Original: ' + cnpj)
print('CNPJ Gerado: ' + cnpj_final)
print('O CNPJ é valido' if cnpj == cnpj_final else 'O CNPJ não é válido')
