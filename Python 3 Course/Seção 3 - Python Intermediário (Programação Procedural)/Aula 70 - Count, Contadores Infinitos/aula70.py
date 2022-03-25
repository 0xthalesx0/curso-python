from types import GeneratorType
variavel = zip('Alo', 'Alo')
print(list(variavel))

print((isinstance(variavel, GeneratorType)))

variavel = ((x, y) for x, y in zip('Alo', 'Alo'))

print((isinstance(variavel, GeneratorType)))