
def master(funcao):
    def slave(*args, **kwargs):
        print('Passando pela master')
        funcao(*args, **kwargs)
    return slave

@master
def fala_oi():
    print('Oioi')


@master
def outra_funcao(msg):
    print(msg)
# fala_oi = master(fala_oi)  ISSO É A PARTE DO DECORADOR
# fala_oi()
# print(type(fala_oi))


outra_funcao('oi')
