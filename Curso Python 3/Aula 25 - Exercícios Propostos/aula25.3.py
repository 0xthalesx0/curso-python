nome = input("Digite seu nome: ")
lennome = nome.__len__()
if lennome <= 4:
    print("Seu nome é curto")
elif 4 < lennome <= 6:
    print("Seu nome é normal")
else:
    print("Seu nome é muito grande")
