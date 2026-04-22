class Veiculo:
    def __init__(self, modelo, placa):
        self.__modelo = modelo
        self.__placa = placa
        self.__alugado = False
    def get_modelo(self):
        return self.__modelo
    def get_placa(self):
        return self.__placa
    def get_alugado(self):
        return self.__alugado
    def alugar(self):
        self.__alugado = True
    def devolver(self):
        self.__alugado = False
        
class Locadora:
    def __init__(self):
        self.veiculos = []
    def cadastrar_veiculo(self):
        modelo = input("Digite o modelo do veículo: ")
        placa = input("Digite a placa do veículo: ")
        veiculo = Veiculo(modelo, placa)
        self.veiculos.append(veiculo)
        print("Veículo cadastrado com sucesso.")
    def encontrar_veiculo(self, placa):
        for veiculo in self.veiculos:
            if veiculo.get_placa() == placa:
                return veiculo
        return None
    def alugar_veiculo_pela_placa(self):
        placa = input("Insira a placa do veículo que deseja alugar: ")
        veiculo = self.encontrar_veiculo(placa)
        if veiculo:
            if not veiculo.get_alugado():
                veiculo.alugar()
                print("Veículo alugado com sucesso.")
            else:
                print("O veículo já está alugado.")
        else:
            print("Veículo não encontrado.")
    def devolver_veiculo(self):
        placa = input("Insira a placa do veículo que deseja devolver: ")
        veiculo = self.encontrar_veiculo(placa)
        if veiculo:
            if veiculo.get_alugado():
                veiculo.devolver()
                print("Veículo devolvido com sucesso.")
            else:
                print("O veículo não está alugado.")
        else:
            print("Veículo não encontrado.")
    def listar_veiculos_disponiveis(self):
        disponiveis = [v for v in self.veiculos if not v.get_alugado()]
        if not disponiveis:
            print("Nenhum veículo disponível no momento.")
            return
        print("Lista de veículos disponíveis:")
        for veiculo in disponiveis:
            print(f"Modelo: {veiculo.get_modelo()} | Placa: {veiculo.get_placa()}")

def main():
    locadora = Locadora()
    while True:
        print("\n" + "="*50)
        print("*** Menu da Locadora ***\n")
        print("1 - Cadastrar um Veículo")
        print("2 - Alugar Veículo pela Placa")
        print("3 - Devolver Veículo")
        print("4 - Listar Veículos Disponíveis")
        print("5 - Sair do Sistema\n")
        
        escolha = input("Digite a opção que você deseja: ")
        print()
        
        if escolha == "1":
            locadora.cadastrar_veiculo()
        elif escolha == "2":
            locadora.alugar_veiculo_pela_placa()
        elif escolha == "3":
            locadora.devolver_veiculo()
        elif escolha == "4":
            locadora.listar_veiculos_disponiveis()
        elif escolha == "5":
            print("Encerrando o sistema.")
            break
        else:
            print("Opção inválida, tente novamente.")
main()