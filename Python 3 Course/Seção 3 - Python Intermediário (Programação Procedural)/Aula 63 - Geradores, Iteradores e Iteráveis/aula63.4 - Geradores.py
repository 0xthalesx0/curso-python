import sys
import time


def gera():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g = gera()

print(next(g))
print(next(g))
print(next(g))
# print(next(g)) -> Isso daria erro -> Então se usa for

l1 = [x for x in range(100000)]
print(type(l1))

l2 = (x for x in range(100000))
print(type(l2))

print(sys.getsizeof(l1))  # Principal diferença é o espaço que ela ocupa
print(sys.getsizeof(l2))
