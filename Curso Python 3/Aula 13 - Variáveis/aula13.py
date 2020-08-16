"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""
nome = 'Luiz'
idade = 32
altura = 1.80
peso = 80
e_maior = idade > 18
data_1 = True
data_atual = 2019

print("Nome: ", nome)
print("Idade: ", idade)
print("Altura: ", altura)
print("É maior: ", e_maior)

imc = peso/(altura**2)
print(nome, "tem", idade, 'anos de idade e seu imc é', imc)
