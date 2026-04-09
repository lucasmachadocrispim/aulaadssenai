class Pessoa:
    def __init__(self, nome=None, idade=None): #Construtora
        if nome is None:
            nome = input("Digite seu nome: ")
            idade = int(input("Digite sua idade: "))
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        print("\n" + "="*50)
        print("Olá", self.nome)
        print("Você tem", self.idade, "anos")
        print("="*50 + "\n")

pessoa1 = Pessoa()
pessoa1.apresentar()
aluna = Pessoa("Ana", 21)
aluna.apresentar()