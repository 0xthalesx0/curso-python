import sys
import time


def exemplo():
    r = []
    for n in range(100):
        r.append(n)
        # time.sleep(0.1)  # Simula o tempo de uma função pesada
    return r


def gera():
    for n in range(100):
        yield n
        time.sleep(0.1)  # Simula o tempo de uma função pesada


e = exemplo()
g = gera()

for v in e:  # Esse mostra todos os valores depois do último ser gerado
    print(v)

for v in g:  # Esse mostra cada valor sem depender dos outros
    print(v)
