
class Usuario:
    def __init__(self, nome, email):
        self.nome = nome.strip()
        self.email = email.strip()

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
