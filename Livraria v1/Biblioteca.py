import re
from Livro import *

livros = []


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
        nome = input("==> Insira o nome do livro: ")
        encontrado = False
        for livro in livros:
            if re.search(nome, livro.titulo, re.IGNORECASE):
                Livro.info(livro)
                encontrado = True
            if not encontrado:
                print("\nNenhum resultado encontrado!")
                break
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
        try:
            estoque = int(input("==> Insira a quantidade mínima de estoque que deseja buscar: "))
            for livro in livros:
                if livro.estoque > estoque:
                    Livro.info(livro)
                else:
                    print("\nNenhum resultado encontrado!")
                    break
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
                  1000)
    livros.append(livro)
