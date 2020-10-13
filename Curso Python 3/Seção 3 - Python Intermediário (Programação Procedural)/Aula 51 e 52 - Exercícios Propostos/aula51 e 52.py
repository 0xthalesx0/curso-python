def funcao1():
    retorno = funcao2(input('Digite seu nome:'))
    print(retorno)


def funcao2(nome):
    return f'Oi {nome}'


def func1(nome):
    print(nome)


def func2(nome):
    return f'oi {nome}'


def func3(nome, saudacao):
    return f'{saudacao} {nome}'


funcao1()
func1(func3('Thales', 'Oi, '))



