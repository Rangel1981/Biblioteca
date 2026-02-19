class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def adicionar_livro(self, livro_objeto):
        self.catalogo.append(livro_objeto)

    def listar_livros(self):
        if not self.catalogo:
            print("Nenhum livro disponível.")
        else:
            for livro in self.catalogo:
                print(livro)

    def emprestar_livro(self, titulo_procurado):
        for livro in self.catalogo:
            if livro.titulo == titulo_procurado:
                if livro.disponivel:
                    livro.disponivel = False
                    print(f"Você emprestou '{livro.titulo}'.")
                    return
        print(f"Livro '{titulo_procurado}' não encontrado ou indisponível.")