num1 = input('digite um número: ')
num2 = input('digite outro número: ')

# isnumeric isdigit isdecimal

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não pude converter os números pra realizar contas.')

