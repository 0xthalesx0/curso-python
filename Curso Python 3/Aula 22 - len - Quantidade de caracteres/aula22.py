usuario = input('Digite seu usuario')
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(qtd_caracteres))

if qtd_caracteres < 6:
    print('Digite pelo menos 6 caracteres')
else:
    print('você foi cadastrado no sistema')

string1 = input('Digite alguma coisa')
string2 = input('Digite outra coisa')

print(f'A quantidade total de caracteres digitados foi {len(string1)+len(string2)}')
