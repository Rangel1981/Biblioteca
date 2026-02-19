from classes import Biblioteca
from livros import Livro

def executar():
    minha_biblioteca = Biblioteca()
    livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia")
    livro2 = Livro("1984", "George Orwell", "Distopia")

    minha_biblioteca.adicionar_livro(livro1)
    minha_biblioteca.adicionar_livro(livro2)

    print("Catálogo da Biblioteca:")
    minha_biblioteca.listar_livros()

    minha_biblioteca.emprestar_livro("1984")
    print("\nCatálogo atualizado:")

    minha_biblioteca.listar_livros()

if __name__ == "__main__":    
    executar()