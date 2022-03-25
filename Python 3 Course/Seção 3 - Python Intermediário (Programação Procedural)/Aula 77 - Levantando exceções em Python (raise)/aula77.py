def divide(n1, n2):
    try:
        return n1/n2
    except ZeroDivisionError as error:
        print('Divisão por 0')
        raise


print(divide(2, 1))
print(divide(2, 0))

try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print('erro')
