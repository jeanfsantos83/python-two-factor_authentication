import random
import time

# Dicionário para armazenar os usuários e suas senhas
usuarios = {
    "admin": {"senha": "password123", "token": None},
    "user1": {"senha": "senha123", "token": None},
    "user2": {"senha": "senha456", "token": None}
}

def gerar_token():
    """Gera um token aleatório de 6 dígitos"""
    return str(random.randint(100000, 999999))

def autenticar_usuario(usuario, senha):
    """Autentica o usuário com a senha"""
    if usuario in usuarios and usuarios[usuario]["senha"] == senha:
        return True
    return False

def autenticar_token(usuario, token):
    """Autentica o token do usuário"""
    if usuario in usuarios and usuarios[usuario]["token"] == token:
        return True
    return False

def login(usuario, senha):
    """Realiza o login do usuário"""
    if autenticar_usuario(usuario, senha):
        token = gerar_token()
        usuarios[usuario]["token"] = token
        print(f"Token de autenticação: {token}")
        return True
    return False

def autenticar(usuario, token):
    """Realiza a autenticação de dois fatores"""
    if autenticar_usuario(usuario, input("Digite a senha: ")) and autenticar_token(usuario, token):
        print("Autenticação bem-sucedida!")
        return True
    print("Autenticação falhou!")
    return False

def main():
    while True:
        print("Menu:")
        print("  1. Login")
        print("  2. Autenticar")
        print("  3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = input("Digite o usuário: ")
            senha = input("Digite a senha: ")
            if login(usuario, senha):
                print("Login realizado com sucesso!")
            else:
                print("Erro ao realizar login!")
        elif opcao == "2":
            usuario = input("Digite o usuário: ")
            token = input("Digite o token de autenticação: ")
            if autenticar(usuario, token):
                print("Autenticação realizada com sucesso!")
            else:
                print("Erro ao realizar autenticação!")
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()