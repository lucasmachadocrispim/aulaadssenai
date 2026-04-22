class Animal:
    def __init__(self, nome, especie, dono):
        self.__nome = nome
        self.__especie = especie
        self.__dono = dono
    def get_nome(self):
        return self.__nome
    def get_especie(self):
        return self.__especie
    def get_dono(self):
        return self.__dono

class Clinica:
    def __init__(self):
        self.animais = []
    def cadastrar_animal(self):
        nome = input("Digite o nome do animal: ")
        especie = input("Digite a espécie do animal: ")
        dono = input("Digite o nome do dono do animal: ")
        animal = Animal(nome, especie, dono)
        self.animais.append(animal)
        print("Animal cadastrado com sucesso.")
    def buscar_animal_por_dono(self):
        dono = input("Insira o nome do dono para buscar os animais: ")
        encontrados = False
        for animal in self.animais:
            if animal.get_dono() == dono:
                print(f"Animal encontrado: Nome: {animal.get_nome()} | Espécie: {animal.get_especie()}")
                encontrados = True
        if not encontrados:
            print("Nenhum animal encontrado para este dono.")
    def listar_animais(self):
        if not self.animais:
            print("Nenhum animal está cadastrado.")
            return
        print("Lista de animais:")
        for animal in self.animais:
            print(f"Nome do Animal: {animal.get_nome()} | Espécie: {animal.get_especie()} | Dono: {animal.get_dono()}")

def main():
    clinica = Clinica()
    while True:
        print("\n" + "="*50)
        print("---Menu da Clinica---\n")
        print("1 - Cadastrar um Animal")
        print("2 - Buscar Animal por Dono")
        print("3 - Listar Animais")
        print("4 - Sair do Sistema\n")
        
        escolha = input("Digite a opção que você deseja: ")
        print()
        
        if escolha == "1":
            clinica.cadastrar_animal()
        elif escolha == "2":
            clinica.buscar_animal_por_dono()
        elif escolha == "3":
            clinica.listar_animais()
        elif escolha == "4":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")

main()