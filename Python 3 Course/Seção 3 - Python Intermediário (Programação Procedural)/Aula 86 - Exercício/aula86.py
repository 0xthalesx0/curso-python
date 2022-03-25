tarefas = []
hist = []


def add_tarefa(tarefa):
    tarefas.append(tarefa)
    hist.clear()


def list_tarefa():
    if tarefas == []:
        print("Lista vazia!")
    else:
        print("Lista de tarefas:")
        for tarefa in tarefas:
            print(tarefa)


def des_tarefa():
    if tarefas == []:
        print('Lista já vazia')
    else:
        hist.append(tarefas.pop())
        print('Ultima tarefa desfeita.')


def ref_tarefa():
    if hist == []:
        print('Não é possível refazer')
    else:
        tarefas.append(hist.pop())
        print('Ultima tarefa refeita.')

while True:
    print('\nBem vindo ao programa!')
    print('1 - Listar tarefa')
    print('2 - Adicionar tarefa')
    print('3 - Desfazer')
    print('4 - Refazer')
    op = int(input('Digite sua opção: '))
    if op == 1:
        list_tarefa()
        input('Pressione enter para continuar...')
    elif op == 2:
        add_tarefa(input('Digite o nome da tarefa: '))
        input('Tarefa inserida. Pressione enter para continuar...')
    elif op == 3:
        des_tarefa()
        input('Pressione enter para continuar...')
    elif op == 4:
        ref_tarefa()
        input('Pressione enter para continuar...')
    else:
        print('Processo terminado')
        break
