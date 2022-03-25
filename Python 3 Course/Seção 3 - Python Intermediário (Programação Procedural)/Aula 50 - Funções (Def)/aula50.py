variavel = 'valor'


def func():
    print(variavel)


def func2():
    global variavel  # Global transforma em global, não é uma boa prática fazer isso no arg
    variavel = 'Outro valor'  # Só altera a variável no escopo (local, a variável não muda)
    print(variavel)


func()
func2()

print(variavel)


def func3():
    print(variavel)
