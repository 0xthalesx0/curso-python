# "O Python reconhece strings como boolean:
# True caso tenha digitado algo,
# ou false caso contrário."

nome = input('Qual o seu nome? ')

if nome:
    print(nome)
else:
    print('Você não digitou nada')

# Mesma função

print(nome or 'você não digitou nada')  # Se for "verdadeiro" (não estiver vazio), print nome, se não, print mensagem
# "Você não digitou nada" É TRUE, POIS É STRING

a = 0  # False
b = None  # False
c = False   # Bruh...
d = []  # False
e = {}  # False
f = 22  # True
g = 'Luiz'  # True

variavel = a or b or c or d or e or f or g

print(variavel)
