# clase14_poo.py

class Libro:
    def __init__(self, titulo, autor, isbn, paginas):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.paginas = paginas
        self.disponible = True  # Por defecto, el libro está disponible

    def mostrar_info(self):
        print("📚 Información del Libro")
        print(f"Título      : {self.titulo}")
        print(f"Autor       : {self.autor}")
        print(f"ISBN        : {self.isbn}")
        print(f"Páginas     : {self.paginas}")
        print(f"Disponible  : {'Sí' if self.disponible else 'No'}")
