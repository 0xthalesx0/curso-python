from time import time, sleep

def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao()
        end_time = time()
        tempo = (end_time - start_time)
        print(f'A função {funcao.__name__} levou {tempo:.1f}s para executar.')
    return interna


@velocidade
def demora():
    for i in range(10):
        print(i)
        sleep(0.255)

demora()
