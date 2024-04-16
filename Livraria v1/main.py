from Biblioteca import *


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
            cadastrar_temp()
            print()
            menu()

        case "1":
            cadastrar_livro()
            print()
            menu()

        case "2":
            listar_livros()
            print()
            menu()

        case "3":
            pesquisar_nome()
            print()
            menu()

        case "4":
            pesquisar_categoria()
            print()
            menu()

        case "5":
            pesquisar_preco()
            print()
            menu()

        case "6":
            pesquisar_estoque()
            print()
            menu()

        case "7":
            somar_estoque()
            print()
            menu()

        case "0":
            print("\nFinalizando sistema...")
            exit()

        case str():
            print("\nOpção inválida!\n")
            menu()


menu()
