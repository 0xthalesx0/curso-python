def func(a1, a2, a3=0):
    a3 = a1
    print(a1, a2, a3)
    return a3


def func2(*args, **kwargs):  # Faz uma tupla (não pode ser alterada)
    args = list(args)  # Transforma a tupla em lista ( () em [] )
    idade = kwargs.get('idade')  #  diferença disso pra só receber o valor é que ele recebe none caso não exista, ao invés de erro
    print(idade)
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    for v in args:
        print(v)


lista = [1, 2, 3, 4, 5]
n1, n2, *n = lista
print(n1, n2, n)


lista2 = [10, 20, 30, 40, 50]
print(*lista2, sep='.')

func2(lista)
func2(*lista)
func2(*lista, *lista2)

func2(*lista, *lista2, nome='luiz', idade=20)  # Nome e idade é um keyword argument (kwargs)
