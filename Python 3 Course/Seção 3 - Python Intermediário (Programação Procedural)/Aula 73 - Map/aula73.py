import sys

sys.path.insert(0, '/Python 3 Course/Seção 3 - Python Intermediário (Programação Procedural)/Fontes')
from dados import lista

# Mesma coisa abaixo:
nova_lista = map(lambda x: x * 2, lista)  # Pra cada elemento de lista
# nova_lista = [x * 2 for x in lista]

print(lista)
print(list(nova_lista))
