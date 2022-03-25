texto = "Python"
novastring = ''

for letra in texto:
    if letra == 't':
        novastring += letra.upper()
    elif letra == 'h':
        novastring += letra.upper()
    else:
        novastring += letra

print(novastring)
