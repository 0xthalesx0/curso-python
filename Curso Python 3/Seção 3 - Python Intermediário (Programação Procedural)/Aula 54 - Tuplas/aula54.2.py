t1 = 1, 2, 3, 4, 5
t1 = list(t1)  # Transforma tupla em lista
t1[1] = 'a'  # Pra poder modificar
t1 = tuple(t1)  # E voltar pra tupla

print(t1)