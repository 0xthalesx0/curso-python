

file = open('aula82.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

# Depois de adicionar, o cursor vai pro fim do arquivo, precisa voltar ele pro começo com seek
file.seek(0, 0)

print('Lendo linhas: ' + file.read())

file.seek(0, 0)
print(file.readline(), end='')
print(file.readline(), end='')
print(file.readline())

file.seek(0, 0)
for linha in file:
    print(linha, end='')

file.close()