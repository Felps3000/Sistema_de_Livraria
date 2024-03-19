# Sistema de Livraria Versão 1.0 BETA 1

produtos = []


def cadastar():
    try:
        produtos.append(Livros(str((input("Insira o título do livro: "))),
                               int((input("Insira o código do livro: "))),
                               str((input("Insira a editora do livro: "))),
                               str((input("Insira a área do livro: "))),
                               int((input("Insira o ano do livro: "))),
                               float((input("Insira o valor do livro: "))),
                               int((input("Insira a quantidade disponível de livros: ")))))
        print()
    except ValueError:
        print("\nO valor inserido não é válido!\n")


# código maluco da loucura pra tentar validar somente os valores corretos :(
# def cadastar():
#     titulo = str(input("Insira o título do livro: "))
#     codigo = input("Insira o código do livro: ")
#     while not codigo.isdigit():
#         codigo = input("Código inválido!\nInsira o código do livro: ")
#     editora = input("Insira a editora do livro: ")
#     area = input("Insira a área do livro: ")
#     ano = input("Insira o ano do livro: ")
#     while not ano.isdigit():
#         ano = input("Valor inválido!\nInsira o ano do livro: ")
#     valor = input("Insira o valor do livro: ")
#     while not valor.isdigit():
#         valor = input("Valor inválido!\nInsira o valor do livro: ")
#     quantidade = input("Insira a quantidade disponível de livros: ")
#     while not quantidade.isdigit():
#         quantidade = input("Valor inválido!\nInsira a quantidade disponível de livros: ")
#
#     produtos.append(Livros(titulo, codigo, editora, area, ano, valor, quantidade))

def listar():
    for i in produtos:
        i.info()


class Livros:
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def info(self):
        print(f">>>>> {self.codigo}\n"
              f"Título/Editora: {self.titulo}/{self.editora}\n"
              f"Categoria: {self.area}\n"
              f"Ano: {self.ano}\n"
              f"Valor: R${self.valor:.2f}\n"
              f"Estoque: {self.estoque} unidades\n"
              f"Valor total em estoque: R${self.soma():.2f}\n"
              )

    def soma(self):
        totalestoque = totalvalor = 0
        for i in range(self.estoque):
            totalestoque += self.estoque
            totalvalor += self.valor
            return totalvalor * totalestoque

    #  def pesquisar(self):


produtos.append(Livros("TITULO", "123456", "EDITORA", "AREA", "1991", 10, 10))


def menu():
    print("Selecione a opção:")
    print("1 – Cadastrar novo livro\n"
          "2 – Listar livros\n"
          "3 – Buscar livros por nome\n"
          "4 – Buscar livros por categoria\n"
          "5 – Buscar livros por preço\n"
          "6 – Busca por quantidade em estoque\n"
          "7 – Valor total no estoque\n"
          "0 – Encerrar atividades\n")

    menuselection = input()
    match menuselection:

        case "1":
            cadastar()
            menu()

        case "2":
            listar()
            menu()

        case "3":
            print("buscar nome")
            menu()

        case "4":
            print("buscar categoria")
            menu()

        case "5":
            print("buscar preço")
            menu()

        case "6":
            print("buscar estoque")
            menu()

        case "7":
            print("valor total estoque")
            menu()

        case "0":
            exit()

        case str():
            print("\nOpção inválida!\n")
            menu()


menu()
