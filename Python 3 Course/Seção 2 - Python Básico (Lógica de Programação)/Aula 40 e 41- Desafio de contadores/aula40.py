"""
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""
cont1 = 0
cont2 = 10
while cont1 < 10:
    print(cont1, cont2)
    cont1 += 1
    cont2 -= 1

# _____________________________

for e, r in enumerate(range(10, 1, -1)):  # e guarda enumerate, r guarda range
    print(e, r)
