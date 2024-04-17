import locale
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")


class Livro:
    def __init__(self, titulo, codigo, editora, area, ano, valor, estoque):
        self.titulo = titulo
        self.codigo = codigo
        self.editora = editora
        self.area = area
        self.ano = ano
        self.valor = valor
        self.estoque = estoque

    def info(self):
        print(f"\n>>>>> Cod#{self.codigo}\n"
              f"Título/Editora: {self.titulo}/{self.editora}\n"
              f"Categoria: {self.area}\n"
              f"Ano: {self.ano}\n"
              f"Valor: {locale.currency(float(self.valor), grouping=True)}\n"
              f"Estoque: {self.estoque} unidade(s)\n"
              f"Valor total em estoque: {locale.currency(float(self.valor * self.estoque), grouping=True)}"
              )
