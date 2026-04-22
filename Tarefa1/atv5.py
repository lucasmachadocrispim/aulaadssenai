class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula
        self.__notas = []
    def get_nome(self):
        return self.__nome
    def get_matricula(self):
        return self.__matricula
    def get_notas(self):
        return self.__notas
    def adicionar_nota(self, nota):
        self.__notas.append(nota)
    def obter_media(self):
        if not self.__notas:
            return 0.0
        return sum(self.__notas) / len(self.__notas)

class Escola:
    def __init__(self):
        self.alunos = []
    def matricular_aluno(self):
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite a matrícula do aluno: ")
        aluno = Aluno(nome, matricula)
        self.alunos.append(aluno)
        print("Aluno matriculado com sucesso.")
    def encontrar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.get_matricula() == matricula:
                return aluno
        return None
    def lancar_nota(self):
        matricula = input("Insira a matrícula do aluno que receberá a nota: ")
        aluno = self.encontrar_aluno(matricula)
        if aluno:
            try:
                nota = float(input("Digite o valor da nota: "))
                aluno.adicionar_nota(nota)
                print("Nota lançada com sucesso.")
            except ValueError:
                print("Valor inválido. A nota deve ser um número.")
        else:
            print("Aluno não encontrado.")
    def calcular_media_do_aluno(self):
        matricula = input("Insira a matrícula do aluno para calcular a média: ")
        aluno = self.encontrar_aluno(matricula)
        if aluno:
            media = aluno.obter_media()
            print(f"A média do aluno {aluno.get_nome()} é: {media:.2f}")
        else:
            print("Aluno não encontrado.")
    def listar_alunos(self):
        if not self.alunos:
            print("Nenhum aluno está matriculado.")
            return
        print("Lista de alunos matriculados:")
        for aluno in self.alunos:
            print(f"Nome: {aluno.get_nome()} | Matrícula: {aluno.get_matricula()} | Notas: {aluno.get_notas()}")

def main():
    escola = Escola()
    while True:
        print("\n" + "="*50)
        print("*** Menu da Escola ***\n")
        print("1 - Matricular Aluno")
        print("2 - Lançar Nota")
        print("3 - Calcular Média do Aluno")
        print("4 - Listar Alunos")
        print("5 - Sair do Sistema\n")
        
        escolha = input("Digite a opção que você deseja: ")
        print()
        
        if escolha == "1":
            escola.matricular_aluno()
        elif escolha == "2":
            escola.lancar_nota()
        elif escolha == "3":
            escola.calcular_media_do_aluno()
        elif escolha == "4":
            escola.listar_alunos()
        elif escolha == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")
main()