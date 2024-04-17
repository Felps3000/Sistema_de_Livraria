import re
from Livro import *

livros = []
alteracao = False


def cadastrar_livro():
    try:
        Livro.titulo = input("==> Insira o título do livro: ")
        Livro.codigo = int(input("==> Insira o código do livro: "))
        Livro.editora = input("==> Insira a editora do livro: ")
        Livro.area = input("==> Insira a área do livro: ")
        Livro.ano = int(input("==> Insira o ano do livro: "))
        Livro.valor = float(input("==> Insira o valor do livro: "))
        Livro.estoque = int(input("==> Insira a quantidade disponível de livros: "))
        livro_cadastrado = Livro(Livro.titulo,
                                 Livro.codigo,
                                 Livro.editora,
                                 Livro.area,
                                 Livro.ano,
                                 Livro.valor,
                                 Livro.estoque)
        livros.append(livro_cadastrado)
        global alteracao
        alteracao = True
        print("\nLivro cadastrado com sucesso!")
    except ValueError:
        print("\nO valor inserido não é válido!")
        print("\nTente Novamente!\n")
        cadastrar_livro()


def listar_livros():
    if livros:
        for livro in livros:
            livro.info()
    else:
        print("Catálogo vazio!")


def pesquisar_nome():
    if livros:
        print("Pesquisar nome")
        nome = input("==> Insira o nome do(s) livro(s): ")
        resultados = []
        for livro in livros:
            if re.search(nome, livro.titulo, re.IGNORECASE):
                resultados.append(livro)
        if resultados:
            for resultado in resultados:
                Livro.info(resultado)
        else:
            print("\nNenhum resultado encontrado!")
    else:
        print("Catálogo vazio!")


def pesquisar_categoria():
    if livros:
        print("Pesquisar categoria")
        categoria = input("==> Insira a categoria do(s) livro(s): ")
        resultados = []
        for livro in livros:
            if re.search(categoria, livro.area, re.IGNORECASE):
                resultados.append(livro)
        if resultados:
            for resultado in resultados:
                Livro.info(resultado)
        else:
            print("\nNenhum resultado encontrado!")
    else:
        print("Catálogo vazio!")


def pesquisar_preco():
    if livros:
        print("Pesquisar preço")
        resultados = []
        try:
            preco = float(input("==> Insira o maior valor que deseja buscar: "))
            for livro in livros:
                if livro.valor < preco:
                    resultados.append(livro)
            if resultados:
                for resultado in resultados:
                    Livro.info(resultado)
            else:
                print("\nNenhum resultado encontrado!")
        except ValueError:
            print("\nO valor inserido não é válido!")
            print("\nTente Novamente!\n")
            pesquisar_preco()
    else:
        print("Catálogo vazio!")


def pesquisar_estoque():
    if livros:
        print("Pesquisar quantidade em estoque")
        resultados = []
        try:
            estoque = int(input("==> Insira a quantidade mínima de estoque que deseja buscar: "))
            for livro in livros:
                if livro.estoque > estoque:
                    resultados.append(livro)
            if resultados:
                for resultado in resultados:
                    Livro.info(resultado)
            else:
                print("\nNenhum resultado encontrado!")
        except ValueError:
            print("\nO valor inserido não é válido!")
            print("\nTente Novamente!\n")
            pesquisar_estoque()
    else:
        print("Catálogo vazio!")


def somar_estoque():
    if livros:
        total = sum(float(livro.estoque * livro.valor) for livro in livros)
        print(f"Valor total do estoque: {locale.currency(total, grouping=True)}")
    else:
        print("Catálogo vazio!")


def cadastrar_temp():
    livro = Livro("Manifesto do Partido Comunista",
                  9788585934231,
                  "Boitempo",
                  "Sociologia/Filosofia",
                  1848,
                  49,
                  1000)
    livros.append(livro)
    livro = Livro("O Estado e a Revolução",
                  8587394991,
                  "Expressão Popular",
                  "Sociologia/Filosofia",
                  1917,
                  38,
                  2000)
    livros.append(livro)


def carregar_arquivo():
    try:
        with open("estoque.csv", "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                dados = linha.split(",")
                codigo, titulo, ano, area, editora, valor, estoque = dados
                livro_cadastrado = Livro(titulo,
                                         int(codigo),
                                         editora,
                                         area,
                                         int(ano),
                                         float(valor.strip("R$")),
                                         int(estoque))
                livros.append(livro_cadastrado)
                global alteracao
                alteracao = True
        print("Arquivo carregado com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")
    except ValueError:
        print("Arquivo em formato inválido!")


def salvar_arquivo(parametro):
    with open("estoque.csv", parametro, encoding="utf-8") as arquivo:
        for livro in livros:
            codigo = livro.codigo
            titulo = livro.titulo
            ano = livro.ano
            area = livro.area
            editora = livro.editora
            valor = livro.valor
            estoque = livro.estoque
            ordem = f"{codigo},{titulo},{ano},{area},{editora},R${valor:.2f},{estoque}\n"
            arquivo.write(ordem)
            global alteracao
            alteracao = False
    print("\nDados salvos com sucesso!")


def atualizar_arquivo():
    if livros:
        try:
            salvar_arquivo("x")  # "x" open for exclusive creation, failing if the file already exists
        except FileExistsError:
            salvar_arquivo("a")  # "a" open for writing, appending to the end of file if it exists
    else:
        print("Catálogo vazio!")


def checar_alteracao():
    if alteracao:
        print("==> Há dados não salvos, deseja salvar antes de sair?\n[S]im | [N]ão")
        match input().lower():
            case "s":
                atualizar_arquivo()
                print("\nFinalizando sistema...")
                exit()
            case "n":
                print("\nFinalizando sistema...")
                exit()
            case str():
                print("\nOpção inválida!\n")
    else:
        print("\nFinalizando sistema...")
        exit()
