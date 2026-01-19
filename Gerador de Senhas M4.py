import random

print("=== CRIAR CONTA NO APLICATIVO ===")

nome = input("Digite seu nome: ")

email = input("Digite seu e-mail: ")
while "@gmail.com" not in email:
    print("E-mail inválido. O e-mail precisa conter @gmail.com")
    email = input("Digite seu e-mail novamente: ")

usuario = input("Digite um nome de usuário: ")

numeros = "0123456789"

aceitou = False

while not aceitou:
    palavra = input("Digite uma palavra para gerar sua senha: ")

    while len(palavra) < 4:
        print("A palavra deve ter pelo menos 4 letras.")
        palavra = input("Digite outra palavra: ")

    senha = palavra.lower()
    senha = senha[0].upper() + senha[1:]

    for i in range(3):
        senha += random.choice(numeros)

    print("\nSenha gerada:", senha)
    print("Tamanho da senha:", len(senha))

    resposta = input("Aceita esta senha? (s/n): ")
    if resposta.lower() == "s":
        aceitou = True
    else:
        print("\nVamos criar uma nova senha.\n")

print("\n=== CONTA CRIADA COM SUCESSO ===")
print("Nome:", nome)
print("E-mail:", email)
print("Usuário:", usuario)

print("\nMensagem de segurança:")
print("Nunca partilhe a sua senha com outras pessoas.")
