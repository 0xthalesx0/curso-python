l1 = ['Luiz', 'João', 'Maria']
l2 = ['Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria', 'Luiz', 'João', 'Maria', ]

print(l1 == l2)
print(set(l1) == set(l2))

"""
if set(l1) == set(l2):
    print('Iguais')
else:
    print('Não iguais')
"""