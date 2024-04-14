# Sistema de Livraria Versão 2.0

import re
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

catalogo = []


class Livros:
    alteracao = False

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
        singular = ""
        if livro["estoque"] > 1:
            singular = "s"

        print(f"\n>>>>> Cod#{livro["codigo"]}\n"
              f"Título/Editora: {livro["titulo"]}/{livro["editora"]}\n"
              f"Categoria: {livro["area"]}\n"
              f"Ano: {livro["ano"]}\n"
              f"Valor: {locale.currency(float(livro["valor"]) * livro["estoque"], grouping=True)}\n"
              f"Estoque: {livro["estoque"]} unidade{singular}\n"
              f"Valor total em estoque: {locale.currency(float(livro["valor"]) * livro["estoque"], grouping=True)}"
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
                str(input("==> Insira o valor do livro: ").strip("r$")).lower(),
                int((input("==> Insira a quantidade disponível de livros: "))))

            cadastro.catalogar()
            Livros.alteracao = True
            print("\nLivro cadastrado com sucesso!")

        except ValueError:
            print("\nO valor inserido não é válido!")

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
                if re.search(titulo, livro["titulo"], re.IGNORECASE):
                    Livros.info(livro)
                else:
                    print("Livro(s) não encontrado(s)!")
                    break
        else:
            print("Catálogo vazio!")

    @staticmethod
    def pesquisar_categoria():
        if catalogo:
            print("Pesquisar categoria")
            categoria = input("==> Insira a categoria do(s) livro(s): ")
            for livro in catalogo:
                if re.search(categoria, livro["area"], re.IGNORECASE):
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
                        print("\nNão existem quantidade igual ou superior de livros que o valor inserido!")
                        break
            else:
                print("Catálogo vazio!")
        except ValueError:
            print("\nO valor inserido não é válido!")

    @staticmethod
    def soma_estoque():
        if catalogo:
            soma = []
            for livro in catalogo:
                soma.append(livro["valor"] * livro["estoque"])
            print(f"Valor total do estoque: {locale.currency(sum(soma), grouping=True)}")
        else:
            print("Catálogo vazio!")

    @staticmethod
    def carregar_arquivo():
        try:
            with open("Livrariav2_estoque.csv", "r", encoding="utf-8") as arquivo:
                linhas = arquivo.readlines()
                for linha in linhas:
                    dados = linha.split(",")
                    codigo, titulo, ano, area, editora, valor, estoque = dados
                    real = valor.lower()
                    livro = Livros(titulo, int(codigo), editora, area, int(ano), float(real.strip("r$")), int(estoque))
                    livro.catalogar()
                    Livros.alteracao = True
            print("Arquivo carregado com sucesso!")
        except FileNotFoundError:
            print("Arquivo não encontrado!")
        except ValueError:
            print("Arquivo em formato inválido!")

    @staticmethod
    def atualizar_arquivo():
        with open("Livrariav2_estoque.csv", "w", encoding="utf-8") as arquivo:
            for livro in catalogo:
                codigo = livro['codigo']
                titulo = livro['titulo']
                ano = livro['ano']
                area = livro['area']
                editora = livro['editora']
                valor = livro['valor']
                estoque = livro['estoque']
                ordem = f"{codigo},{titulo},{ano},{area},{editora},{valor},{estoque}\n"
                arquivo.write(ordem)
        print("\nDados salvos com sucesso!")

    @staticmethod
    def check_alteracao():
        if Livros.alteracao:
            print("==> Há dados não salvos, deseja salvar antes de sair?\n[S]im | [N]ão")
            match input().lower():
                case "s":
                    Livros.atualizar_arquivo()
                    print("\nFinalizando sistema...")
                    exit()
                case "n":
                    print("\nFinalizando sistema...")
                    exit()
                case str():
                    print("\nOpção inválida!\n")
                    menu()
        else:
            print("\nFinalizando sistema...")
            exit()


def menu():
    print("Selecione a opção:\n"
          "1 – Cadastrar novo livro\n"
          "2 – Listar livros\n"
          "3 – Buscar livros por nome\n"
          "4 – Buscar livros por categoria\n"
          "5 – Buscar livros por preço\n"
          "6 – Busca por quantidade em estoque\n"
          "7 – Valor total no estoque\n"
          "8 – Carregar estoque\n"
          "9 – Atualizar arquivo de estoque\n"
          "0 – Encerrar atividades\n")

    match input():

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

        case "8":
            Livros.carregar_arquivo()
            print()
            menu()

        case "9":
            Livros.atualizar_arquivo()
            print()
            menu()

        case "0":
            Livros.check_alteracao()

        case str():
            print("\nOpção inválida!\n")
            menu()


menu()
