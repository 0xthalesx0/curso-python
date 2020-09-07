variavel = ["A", 'B', "C"]

for valor in variavel:
    print(valor)
    break

variavel = "João"
if variavel.startswith("J"):
    print(variavel)

for valor in variavel:  # Se o laço terminar, else.
    if valor.lower().startswith('J'):
        break
else:  # Se não dar break, isso aqui executa (só break, continue n funfa)
    print("Não existe uma palavra que começa com J.")
