def saudacao(msg='Olá', nome='Usuário'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    print(msg, nome)
    return f'{msg} {nome}'


saudacao('Olá', 'Luiz Otávio')
saudacao()
saudacao(nome='Zezinho', msg='Oi')

variavel = saudacao()
print(variavel)
