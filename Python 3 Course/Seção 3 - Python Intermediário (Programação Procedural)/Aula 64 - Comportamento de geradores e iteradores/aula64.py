# lists, tuples, str -> sequences -> iteravel
nome = 'Luiz Otávio'

gerador = (letra for letra in nome)
# for letra in nome:  # converte a string em iterável temporariamente, dá next nele até dar erro (except)
#    print(letra)

# print('#' * 80)

# for letra in nome:  # Converte de novo, então não esgota
#    print(letra)

# print(nome)

iterador = iter(nome)
try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(gerador))
    print(next(gerador))
    print(next(gerador))
    print(next(gerador))
except:  # Escapa o erro que dar next quando já acabou o iter lança
    pass

print('Cadê os valores?')
for valor in iterador:
    print(valor)  # Isso não volta valores, porque o iterador já foi consumido acima

for v in gerador:  # Idêntico, são consumidos
    print(v)
