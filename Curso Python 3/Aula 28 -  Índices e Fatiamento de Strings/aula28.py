# positivos     [012345678]
texto         = "Python S2"
# negativos    -[987654321]
print(texto[0])
print(texto[6])
# print(texto[9]) Esse é um erro, não tem char 9

novastring = texto[2:6]  # O 6 não é incluso nisso, tipo um <
print(novastring)
novastring = texto[:6]  # Pega de 0 a 5
print(novastring)
novastring = texto[7:]  # Pega a partir do 7
print(novastring)
novastring = texto[:-1]  # Arranca o ultimo caractere da string
print(novastring)
novastring = texto[-9:8:2]  # Step, de quantos em quantos ele vai pular nesse terceiro espaço
print(novastring)
novastring = texto[0::3]  # Step
print(novastring)
