"""
CPF = 168.995.350-09
-------------------------------------------------
1 * 10 = 10            #    1 * 11 = 11 <-
6 * 9 = 54             #    6 * 10 = 60
8 * 8 = 64             #    8 * 9 = 72
9 * 7 = 63             #    9 * 8 = 72
9 * 6 = 54             #    9 * 7 = 63
5 * 5 = 25             #    5 * 6 = 30
3 * 4 = 12             #    3 * 5 = 15
5 * 3 = 15             #    5 * 4 = 20
0 * 2 = 0              #    0 * 3 = 0
                       # -> 0 * 2 = 0
        297            #            343
11 - (297 % 11) = 11   #     11 - (343 % 11) = 9
11 > 9 = 0             #
Dígito 1 = 0           #    Dígito 2 = 9
"""
cpf = input("Digite seu CPF (Apenas números): ")

if cpf.isnumeric():
    # = int(cpf)
    ...
else:
    print("Digite um cpf válido!")

soma1 = 0
soma2 = 0
novocpf = cpf[:9]

# Dígito 1

for e, cont in enumerate(range(10, 1, -1)):
    soma1 = soma1 + int(cpf[e]) * cont

val = ((soma1 * 10) % 11)
dig1 = val if val != 10 else 0
print(dig1)
novocpf = novocpf + str(dig1)

# Digito 2
for f, cont2 in enumerate(range(11, 1, -1)):
    soma2 = soma2 + int(cpf[f]) * cont2

val = ((soma2 * 10) % 11)
dig2 = val if val != 10 else 0

print(dig2)
novocpf = novocpf + str(dig2)

if novocpf == cpf:
    print("CPF válido!")
else:
    print("CPF inválido!")

