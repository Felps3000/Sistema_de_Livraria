# **Trabalho Prático 1 – Sistema de livraria .v2**
## **Protótipo 2**
### O cliente ficou parcialmente satisfeito com o produto entregue, no entanto após alguns usos sentiu a necessidade de algumas novas funcionalidades:

> Requisito 2.1: O cliente deseja que seja implementada uma funcionalidade para
carregar os livros cadastrados através de um arquivo txt (nova opção 8 - carregar
estoque). Quando indagado sobre como as informações serão postas no arquivo eles
passaram o seguinte exemplo:</p>

` 3426,compiladores,2012,computação,pearson,R$135.50,50 `<br>
` 2631,sistemas digitais,2017,computação,liber,R$99.90,30 ` <br>
` 9680,senhor dos aneis: a sociedade do anel,2005,fantasia,harper,R$35.00,120 ` <br>

ou seja o formato pode ser visto como:

` <codigo>,<titulo>,<ano>,<área/gênero>,<editora>,R$<valor>,<qtd em estoque> `

> Requisito 2.2: Outra solicitação do cliente é que todas as modificações feitas através do sistema sejam guardadas novamente no arquivo txt. Tal ação deve ocorrer através de uma opção no menu (Opção 9 - Atualizar arquivo de estoque). Ao encerrar o sistema (Opção 0 - Encerrar atividades) o usuário deve ser indagado se quer atualizar o arquivo.

## **Protótipo 1**
### Uma livraria solicitou um software para cadastro de seus produtos (livros). Durante os processos iniciais de projeto foram levantados os seguintes requisitos para o software:

> Requisito 1.1: O cadastro dos produtos precisa guardar as seguintes informações:
- Titulo
- Código
- Editora
- Área
- Ano
- Valor
- Quantidade em Estoque

*Os dados dos livros devem ser armazenados em algum tipo de estrutura de dados como por exemplo vetores ou listas.*

> Requisito 1.2: Listar todos os livros que foram cadastrados e suas informações. O seguinte exemplo foi dado:

`>>>>> Cod#0301`<br>
`Titulo/Editora: Compiladores/Pearson`<br>
`Categoria: Computação`<br>
`Ano: 2016`<br>
`Valor: R$ 85,00`<br>
`Estoque: 125 unidades`<br>
`Valor total em estoque: R$ 10625,00`<br>

`>>>>>> Cod#1203`<br>
`Titulo/Editora: Engenharia de Software/Pressman`<br>
`Categoria: Computação`<br>
`Ano: 2011`<br>
`Valor: R$ 78`<br>
`Estoque: 100 unidades`<br>
`Valor total em estoque: R$ 7800,00`<br>

> Requisito 1.3: Algumas formas de busca e filtragem de livros conforme suas informações:
- Busca pelo nome do livro.
- Informar quais livros tem preço menor que um valor.
- Apresentar livros de uma categoria específica.
- Buscar livros com valor de estoque maior que o indicado pelo usuário.
  
> Requisito 1.4: Uma interface de usuário onde seja possível selecionar as ações disponíveis. O sistema deve permitir que sejam executadas múltiplas ações. O seguinte exemplo foi dado:

`1 – Cadastrar novo livro`<br>
`2 – Listar livros`<br>
`3 – Buscar livros por nome`<br>
`4 – Buscar livros por categoria`<br>
`5 – Buscar livros por preço`<br>
`6 – Busca por quantidade em estoque`<br>
`7 – Valor total no estoque`<br>
`0 – Encerrar atividades`<br>
