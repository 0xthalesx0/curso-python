def divide(n1, n2):
    if n2 == 0:
        raise ValueError("n2 não pode ser 0")
    return n1/n2


print(divide(2,1))
try:
    print(divide(2, 0))
except ValueError as error:
    print(error)
