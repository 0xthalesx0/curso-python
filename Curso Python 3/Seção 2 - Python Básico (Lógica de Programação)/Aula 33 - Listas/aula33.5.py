secreto = 'cu'
digitadas = []
chances = 3

while True:
    if chances < 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra in secreto:
        print(f'A letra {letra} existe na palavra secreta.')
        digitadas.append(letra)
    else:
        print(f'A letra não existe na palavra secreta')
        print(f'Você ainda tem {chances} chances!')
        chances -= 1

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print(f'Você ganhou! a palavra era: {secreto_temp}')
        break
    else:
        print(f'A palavra está assim: {secreto_temp}')
    print(digitadas)

