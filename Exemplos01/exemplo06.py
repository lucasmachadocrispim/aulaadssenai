class Forma:
    def area(self):
        pass
class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def area(self):
        return self.largura * self.altura
class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura)/2
class Trapezio(Forma):
    def __init__(self, base_1, base_2, altura):
        self.base_1 = base_1
        self.base_2 = base_2
        self.altura = altura
    def area(self):
        return(((self.base_1 + self.base_2) * self.altura) / 2)
formas = [Retangulo(10,5), Triangulo(10,5), Trapezio(10, 5, 5)]
for forma in formas:
    print("Área", forma.area())