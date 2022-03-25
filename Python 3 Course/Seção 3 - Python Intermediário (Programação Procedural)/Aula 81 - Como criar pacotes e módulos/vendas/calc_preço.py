from vendas.formato import preco


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))
    return preco.real(r) if formata else r





def reducao(valor, porcentagem, formata=False):
    return valor - (valor * (porcentagem / 100))