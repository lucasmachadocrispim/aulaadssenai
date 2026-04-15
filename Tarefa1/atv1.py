class Livro:
    def __init__(self, titulo, autor, disponivel):
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
            
        else:
            print("Livro não encontrado")
    def devolver_livro(self):
        return self.a * self.b
    def listar_livros(self):
        return self.a / self.b