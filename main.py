
from usuario import Usuario


class SistemaCadastro:
    def __init__(self):
        self.usuarios = []

    def cadastrar_usuario(self):
        print("\n" + "=" * 50)
        print("BEM-VINDO(A) AO CADASTRO DE USUÁRIOS")
        print("=" * 50)

        nome = input("Digite o nome de usuário desejado: ").strip()

        if not nome:
            print("O nome não pode ficar vazio.")
            return

        for usuario in self.usuarios:
            if usuario.nome.casefold() == nome.casefold():
                print("Nome de usuário indisponível.")
                return

        email = input("Digite seu e-mail: ").strip()

        if not email:
            print("O e-mail não pode ficar vazio.")
            return

        for usuario in self.usuarios:
            if usuario.email.casefold() == email.casefold():
                print("Este e-mail já está sendo utilizado.")
                return

        novo_usuario = Usuario(nome, email)
        self.usuarios.append(novo_usuario)

        print("Usuário cadastrado com sucesso!")

    def listar_usuarios(self):
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return

        print("\n--- USUÁRIOS CADASTRADOS ---")

        for i, usuario in enumerate(self.usuarios, start=1):
            print(
                f"{i}. Nome: {usuario.nome} | "
                f"E-mail: {usuario.email}"
            )

    def buscar_usuario(self):
        busca = input("Digite o nome do usuário: ").strip()

        for usuario in self.usuarios:
            if usuario.nome.casefold() == busca.casefold():
                print("\nUsuário encontrado:")
                usuario.exibir_dados()
                return

        print("Usuário não encontrado.")

    def menu(self):
        print("\n" + "=" * 50)
        print("SISTEMA DE CADASTRO DE USUÁRIOS")
        print("=" * 50)

        while True:
            print("\n1 - Cadastrar usuário")
            print("2 - Listar usuários")
            print("3 - Buscar usuário")
            print("0 - Encerrar o sistema")

            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                self.cadastrar_usuario()
            elif opcao == "2":
                self.listar_usuarios()
            elif opcao == "3":
                self.buscar_usuario()
            elif opcao == "0":
                print("Sistema encerrado!")
                break
            else:
                print("Opção inválida. Tente novamente.")


def main():
    sistema = SistemaCadastro()
    sistema.menu()


if __name__ == "__main__":
    main()
