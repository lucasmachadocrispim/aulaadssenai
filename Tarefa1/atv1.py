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
        self.__livros = []

    def cadastrar_livro(self):
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        livro = Livro(titulo, autor)
        return self.a + self.b
    def emprestar_livro(self):
        return self.a - self.b
    def devolver_livro(self):
        return self.a * self.b
    def listar_livros(self):
        return self.a / self.b