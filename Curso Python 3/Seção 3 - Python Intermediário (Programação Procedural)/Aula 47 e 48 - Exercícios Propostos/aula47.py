def salve(nome, saudacao):
    print(f'{saudacao}, {nome}!')


def soma(n1, n2, n3):
    print(f'A soma é: {(n1+n2+n3)}')


def percent(n, perc):
    n = n + (n * (0.01 * perc))
    return n


def FizzBuzz(n):
    fizz = n % 3 == 0
    buzz = n % 5 == 0
    fizzbuzz = fizz and buzz
    if fizzbuzz:
        return 'FizzBuzz'
    elif fizz:
        return 'Fizz'
    elif buzz:
        return 'Buzz'
    else:
        return n


