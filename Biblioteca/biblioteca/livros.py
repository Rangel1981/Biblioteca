class Livro:
    def __init__ (self, titulo, autor, genero):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.disponivel = True

    def __str__(self):
        return f"{self.titulo} por {self.autor} - {self.genero} - {'Disponível' if self.disponivel else 'Indisponível'}"
