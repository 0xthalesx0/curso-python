s1 = {1, 2, 3, 4, 5, 6}  # Sets não possuem indexes, um set em branco é um dicionário
s1.add(7)
s1.update('a')  # mesma coisa que add
s1.update('Python')  # Colocaria cada letra iterada separadamente na lista

s2 = set()
s2.update([1, 2, 3, 4, 5], {4, 5, 6, 7, 8})  # 4 e 5 não entram 2 vezes, é unico pra cada valor

l1 = [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 5, 6, 7, 'Luiz', 'Luiz']
l1 = set(l1)  # Transforma em set pra remover duplicatas, podem zuar a ordem da lista
l1 = list(l1)  # Volta pra lista, sem duplicatas

print(s1)
print(type(s1))
print(l1)
