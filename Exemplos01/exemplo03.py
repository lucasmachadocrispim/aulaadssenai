class Calculadora:
    def __init__(self, a=None, b=None):
        if a is None:
            a = float(input("Digite o valor de 'a': "))
        if b is None:
            b = float(input("Digite o valor de 'b': "))
        self.a = a
        self.b = b
    def adicionar(self):
        return self.a + self.b
    def subtrair(self):
        return self.a - self.b
    def multiplicar(self):
        return self.a * self.b
    def dividir(self):
        if self.a == 0 or self.b == 0:
            print("Não é possivel dividir com 0")
            pass
        return self.a / self.b
calc = Calculadora()
print(calc.adicionar())
print(calc.subtrair())
print(calc.multiplicar())
print(calc.dividir())