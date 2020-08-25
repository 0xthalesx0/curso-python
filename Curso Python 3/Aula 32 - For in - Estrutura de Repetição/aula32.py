texto = 'Python'

"""
c = 0
while c < len(texto):
    print(texto[c])
    c += 1
"""
"""
for letra in texto:
    print(letra)
"""
for n, letra in enumerate(texto):
    print(n, letra)

print('############')

# range: Start = 0, Stop = X, Step = 1
for num in range(10):
    print(num)

print('############')

for num in range(20, 10, -1):
    print(num)

print('############')

for n in range(100):
    if n % 8 == 0:
        print(n)
