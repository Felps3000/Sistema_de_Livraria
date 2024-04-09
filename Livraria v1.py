# Sistema de Livraria Versão 1.0 BETA 1

produtos = []


def cadastrar():
    try:
        produtos.append(Livros(str((input("Insira o título do livro: "))),
                               int((input("Insira o código do livro: "))),
                               str((input("Insira a editora do livro: "))),
                               str((input("Insira a área do livro: "))),
                               int((input("Insira o ano do livro: "))),
                               float((input("Insira o valor do livro: "))),
                               int((input("Insira a quantidade disponível de livros: ")))))
        print("\nLivro cadastrado com sucesso!\n")
    except ValueError:
        print("\nO valor inserido não é válido!\n")

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
        print(f">>>>> Cod#{self.codigo}\n"
              f"Título/Editora: {self.titulo}/{self.editora}\n"
              f"Categoria: {self.area}\n"
              f"Ano: {self.ano}\n"
              f"Valor: R$ {self.valor:.2f}\n"
              f"Estoque: {self.estoque} unidades\n"
              f"Valor total em estoque: R$ {self.valor * self.estoque:.2f}\n"
              )

produtos.append(Livros("BUNDA", "123456", "EDITORA", "AREA", "1991", 10, 10))
produtos.append(Livros("TITULO2", "78910111213", "EDITORA2", "AREA2", "1992", 20, 20))
produtos.append(Livros("TITULO3", "14151617", "EDITORA3", "AREA3", "1993", 30, 30))
produtos.append(Livros("TITULO3", "14151617", "EDITORA3", "AREA3", "1993", 40, 40))


def pesquisar(atributo, valor):
    match atributo:
        case "nome":
            for livro in produtos:
                if valor.lower() in livro.titulo.lower():
                    return print(livro.info())
                    break
                else:
                    print("Livro não encontrado!\n")
                    break

def menorPreco(preco):
    for livro in produtos:
        while livro.valor < preco:
            print(livro.info())


def listar():
    for i in produtos:
        i.info()


def somar_estoque():
    total = sum(livros.valor * livros.estoque for livros in produtos)
    print(f"Valor total no estoque: R${total:.2f}\n")


def menu():
    print("Selecione a opção:\n"
          "1 – Cadastrar novo livro\n"
          "2 – Listar livros\n"
          "3 – Buscar livros por nome\n"
          "4 – Buscar livros por categoria\n"
          "5 – Buscar livros por preço\n"
          "6 – Busca por quantidade em estoque\n"
          "7 – Valor total no estoque\n"
          "0 – Encerrar atividades\n")


    match input():

        case "1":
            cadastrar()
            menu()

        case "2":
            listar()
            menu()

        case "3":
            pesquisar("nome",str(input("Insira o nome do livro: ")))
            menu()

        case "4":
            print("buscar categoria")
            menu()

        case "5":
            menorPreco(float(input("Insira o valor: ")))
            menu()

        case "6":
            print("buscar estoque")
            menu()

        case "7":
            somar_estoque()
            menu()

        case "0":
            exit()

        case str():
            print("\nOpção inválida!\n")
            menu()


menu()
