def funcao(var):
    print(var)
    return var
    # print('isso não será executado')


def divisao(n1, n2):
    if n2 == 0:
        return

    return n1 / n2


variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('nenhum valor')

divide = divisao(8, 2)
print(divide)

divide = divisao(8, 0)
print(divide)