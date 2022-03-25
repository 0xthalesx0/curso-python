#        Índices
#        0123456789.......................33
frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
contador = 0
novastring = ''

input_do_usuario = input('Qual letra deseja colocar maiúscula: ')

while contador < 34:
    # print(frase[contador], contador)
    letra = frase[contador]
    if letra.upper() == input_do_usuario.upper():
        novastring += input_do_usuario.upper()
    else:
        novastring += letra
    contador += 1

print(novastring)
