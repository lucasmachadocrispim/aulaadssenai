class Livro:
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__disponivel = True
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_disponivel(self):
        return self.__disponivel
    def emprestar(self):
        self.__disponivel = False
    def devolver(self):
        self.__disponivel = True
class Biblioteca:
    def __init__(self):
        self.livros = []
    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livro = Livro(titulo, autor)
        self.livros.append(livro)
        print("Livro cadastrado com sucesso")
    def encontrar_livro(self, titulo):
        for livro in self.livros:
            if livro.get_titulo() == titulo:
                return livro
            return None
    def emprestar_livro(self):
        titulo = input("Insira o título do livro que deseja emprestar: ")
        livro = self.encontrar_livro(titulo)
        if livro:
            if livro.get_disponivel():
                livro.emprestar()
                print("Livro emprestado com sucesso.")
            else:
                print("O livro não está disponível para empréstimo.")
        else:
            print("Livro não encontrado.")
    def devolver_livro(self):
        titulo = input("Insira o título do livro que deseja devolver: ")
        livro = self.encontrar_livro(titulo)
        if livro:
            if livro.get_disponivel():
                
                print("O livro não está disponível para devolução.")
            else:
                livro.devolver()
                print("Livro devolvido com sucesso.")
        else:
            print("Livro não encontrado.")
    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro está cadastrado")
            return
        print("Lista de livros:")
        for livro in self.livros:
            status = "Disponível" if livro.get_disponivel() else "Indisponivel"
            print("Nome do livro:", livro.get_titulo(), " -  Nome do autor:", livro.get_autor(), " -  Status:", status)
def main():
    biblioteca = Biblioteca()
    while True:
        print("\n" + "="*50)
        print("---Menu da Biblioteca---\n")
        print("1 - Cadastrar um Livro")
        print("2 - Emprestar um Livro")
        print("3 - Devolver um Livro")
        print("4 - Listar Livros")
        print("5 - Sair do Sistema\n")
        escolha = input("Digite a opção que você deseja: ")
        print()
        if escolha == "1":
            biblioteca.cadastrar_livro()
        elif escolha == "2":
            biblioteca.emprestar_livro()
        elif escolha == "3":
            biblioteca.devolver_livro()
        elif escolha == "4":
            biblioteca.listar_livros()
        elif escolha == "5":
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida, tente novamente.")
main()