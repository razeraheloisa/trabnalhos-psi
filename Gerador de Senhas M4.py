import random

print("=== CRIAR CONTA NO APLICATIVO ===")

# Dados do usuário
nome = input("Digite seu nome: ")
email = input("Digite seu e-mail: ")
usuario = input("Digite um nome de usuário: ")

# Listas de letras para senha fácil
consoantes = "bcdfghjklmnpqrstvwxyz"
vogais = "aeiou"

senha = ""

# Gera uma senha fácil de decorar (5 letras)
for i in range(5):
    if i % 2 == 0:
        senha += random.choice(consoantes)
    else:
        senha += random.choice(vogais)

# Primeira letra maiúscula
senha = senha.capitalize()

print("\n=== CONTA CRIADA COM SUCESSO ===")
print("Nome:", nome)
print("E-mail:", email)
print("Usuário:", usuario)
print("Senha gerada:", senha)
print("Tamanho da senha:", len(senha))
