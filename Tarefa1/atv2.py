class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = float(preco)
        self.__quantidade = int(quantidade)

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def adicionar_quantidade(self, valor):
        self.__quantidade += valor

    def remover_quantidade(self, valor):
        self.__quantidade -= valor

class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar_produto(self):
        nome = input("Digite o nome do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite quantos produtos estão disponíveis: ")
        produto = Produto(nome, preco, quantidade)
        self.produtos.append(produto)
        print("Produto cadastrado com sucesso")

    def encontrar_produto(self, nome):
        for produto in self.produtos:
            if produto.get_nome() == nome:
                return produto
        return None

    def adicionar_quantidade(self):
        nome = input("Insira o nome do produto que deseja adicionar quantidade: ")
        produto = self.encontrar_produto(nome)
        if produto:
            quantidade_atual = produto.get_quantidade()
            print(f"Quantidade de {produto.get_nome()} = {quantidade_atual}")
            valor = int(input("Insira quanto adicionar: "))
            produto.adicionar_quantidade(valor)
            print("Valor adicionado ao produto.")
        else:
            print("Produto não encontrado.")

    def remover_quantidade(self):
        nome = input("Insira o nome do produto que deseja remover quantidade: ")
        produto = self.encontrar_produto(nome)
        if produto:
            quantidade_atual = produto.get_quantidade()
            print(f"Quantidade de {produto.get_nome()} = {quantidade_atual}")
            if quantidade_atual > 0:
                valor = int(input("Insira quanto remover: "))
                if valor > quantidade_atual:
                    print("Não é possível remover esta quantidade.")
                else:
                    produto.remover_quantidade(valor)
                    print("Valor removido do produto.")
            else:
                print("Não é possivel remover mais produtos.")
        else:
            print("Produto não encontrado.")

    def listar_produtos(self):
        if not self.produtos:
            print("Nenhum produto está cadastrado")
            return
        print("Lista de produtos:")
        for produto in self.produtos:
            preco = produto.get_preco()
            print(f"Nome do Produto: {produto.get_nome()} - Valor: R${preco:.2f} - Quantidade: {produto.get_quantidade()}")

def main():
    estoque = Estoque()
    while True:
        print("\n" + "="*50)
        print("---Menu da Loja---\n")
        print("1 - Cadastrar um Produto")
        print("2 - Adicionar Quantidade")
        print("3 - Remover Quantidade")
        print("4 - Listar Produtos")
        print("5 - Sair do Sistema\n")
        escolha = input("Digite a opção que você deseja: ")
        print()
        if escolha == "1":
            estoque.cadastrar_produto()
        elif escolha == "2":
            estoque.adicionar_quantidade()
        elif escolha == "3":
            estoque.remover_quantidade()
        elif escolha == "4":
            estoque.listar_produtos()
        elif escolha == "5":
            print("Encerrando o sistema")
            break
        else:
            print("Opção inválida, tente novamente.")

main()