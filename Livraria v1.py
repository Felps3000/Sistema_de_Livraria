# Sistema de Livraria Versão 1.0

catalogo = []


class Livros:
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def catalogar(self):
        livro = {
            "titulo": self.titulo,
            "codigo": self.codigo,
            "editora": self.editora,
            "area": self.area,
            "ano": self.ano,
            "valor": self.valor,
            "estoque": self.estoque
        }

        catalogo.append(livro)

    @staticmethod
    def info(livro):
        print(f"\n>>>>> Cod#{livro['codigo']}\n"
              f"Título/Editora: {livro['titulo']}/{livro['editora']}\n"
              f"Categoria: {livro['area']}\n"
              f"Ano: {livro['ano']}\n"
              f"Valor: R$ {livro['ano']:.2f}\n"
              f"Estoque: {livro['estoque']} unidades\n"
              f"Valor total em estoque: R$ {livro['valor'] * livro['estoque']:.2f}"
              )

    @staticmethod
    def cadastrar():
        try:
            cadastro = Livros(
                str((input("==> Insira o título do livro: "))),
                int((input("==> Insira o código do livro: "))),
                str((input("==> Insira a editora do livro: "))),
                str((input("==> Insira a área do livro: "))),
                int((input("==> Insira o ano do livro: "))),
                float((input("==> Insira o valor do livro: "))),
                int((input("==> Insira a quantidade disponível de livros: "))))

            cadastro.catalogar()
            print("\nLivro cadastrado com sucesso!")

        except ValueError:
            print("\nO valor inserido não é válido!")

    @staticmethod
    def cadastro_temp():
        cadastro1 = Livros(
            "bicho",
            123,
            "jesus",
            "biologia",
            123,
            123,
            123
        )

        cadastro2 = Livros(
            "bicho",
            123,
            "deus",
            "humanidade",
            123,
            123,
            123
        )

        cadastro1.catalogar()
        cadastro2.catalogar()

    @staticmethod
    def listar():
        if catalogo:
            for i, livros in enumerate(catalogo, start=1):
                Livros.info(livros)
        else:
            print("Catálogo vazio!")

    @staticmethod
    def pesquisar_nome():
        if catalogo:
            print("Pesquisar nome")
            titulo = input("==> Insira o nome do livro: ")
            for livro in catalogo:
                if livro["titulo"].lower() == titulo.lower():
                    Livros.info(livro)
                else:
                    print("Livro não encontrado!")
                    break
        else:
            print("Catálogo vazio!")

    @staticmethod
    def pesquisar_categoria():
        if catalogo:
            print("Pesquisar categoria")
            categoria = input("==> Insira a categoria do(s) livro(s): ")
            for livro in catalogo:
                if livro["area"].lower() == categoria.lower():
                    Livros.info(livro)
                else:
                    print("Categoria não encontrada!")
                    break
        else:
            print("Catálogo vazio!")

    @staticmethod
    def pesquisar_preco():
        try:
            if catalogo:
                print("Pesquisar preço")
                preco = float(input("==> Insira o menor valor que deseja buscar: "))
                for livro in catalogo:
                    if float(livro["valor"]) <= preco:
                        Livros.info(livro)
                    else:
                        print("Não existem livros com o valor menor que o inserido!")
                        break
            else:
                print("Catálogo vazio!")
        except ValueError:
            print("\nO valor inserido não é válido!")

    @staticmethod
    def pesquisa_estoque():
        try:
            if catalogo:
                print("Pesquisar quantidade em estoque")
                quantidade = float(input("==> Insira a quantidade de estoque que deseja buscar: "))
                for livro in catalogo:
                    if float(livro["estoque"]) >= quantidade:
                        Livros.info(livro)
                    else:
                        print("Não existem livros com o valor menor que o inserido!")
                        break
            else:
                print("Catálogo vazio!")
        except ValueError:
            print("\nO valor inserido não é válido!")

    @staticmethod
    def soma_estoque():
        if catalogo:
            soma = 0
            for livro in catalogo:
                soma += float(livro["valor"] * livro["estoque"])
            print(f"Valor total do estoque: R${soma:.2f}")
        else:
            print("Catálogo vazio!")


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

        case "55":
            Livros.cadastro_temp()
            print()
            menu()

        case "1":
            Livros.cadastrar()
            print()
            menu()

        case "2":
            Livros.listar()
            print()
            menu()

        case "3":
            Livros.pesquisar_nome()
            print()
            menu()

        case "4":
            Livros.pesquisar_categoria()
            print()
            menu()

        case "5":
            Livros.pesquisar_preco()
            print()
            menu()

        case "6":
            Livros.pesquisa_estoque()
            print()
            menu()

        case "7":
            Livros.soma_estoque()
            print()
            menu()

        case "0":
            print("\nFinalizando sistema...")
            exit()

        case str():
            print("\nOpção inválida!\n")
            menu()


menu()
