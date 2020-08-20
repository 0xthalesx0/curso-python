a = 2
b = 2
c = 3
if a == b and b < c:
    print('true')
else:
    print('false')

comparacao1 = a == b
comparacao2 = b > c

falso = comparacao1 and comparacao2
verdadeiro = comparacao1 or comparacao2
inversao = not comparacao1

print(inversao)
d = ''
if not d:
    print('Por favor, preencha o valor de D')

if not b > int(d):
    print('B é maior do que A')
else:
    print('A é maior do que B')


nome = 'Luiz Otavio'
if 'u' in nome:
    print("Existe a letra U no seu nome.")

if 'vio' not in nome:
    print("executei.")
else:
    print('existe o texto.')

