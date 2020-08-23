try:
    num = int(input("Digite um numero inteiro: "))
    e_par = (num % 2) == 0
    if e_par:
        print(f"O numero {num} é par")

    else:
        print(f"O numero {num} é impar")
except:
    print("Digite um número inteiro válido!")
