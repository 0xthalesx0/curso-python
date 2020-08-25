contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break  # isso faz ele sair do laço SEM deixar a expressão do While falsa
    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else.')  # Então essa mensagem não aparece
print('Isso será executado')
