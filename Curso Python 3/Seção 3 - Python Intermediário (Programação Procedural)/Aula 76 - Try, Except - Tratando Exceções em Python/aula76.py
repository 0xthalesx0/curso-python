try:
    a = {}
    print(a)
except NameError as erro:
    print(f"Erro: {erro}")
except (IndexError, KeyError) as erro:
    print(f"Erro de índice: {erro}")
except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
else:
    print("Tudo certo!")
finally:
    print("Acabou o try")
print("Continuando")