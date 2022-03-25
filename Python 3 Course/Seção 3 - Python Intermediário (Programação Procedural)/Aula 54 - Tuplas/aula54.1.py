t1 = 1, 2, 'a', 'b'
t2 = 3, 4, 'c', 'd'
t3 = t1 + t2
t4 = t1 * 20

print(t3)

n1, n2, n3, *_, nu = t3

print(n3)
print(nu)
print(_)
print(t4)
