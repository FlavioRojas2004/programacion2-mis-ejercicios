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
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)
print(f"\nEl autor del primer libro es: {libro1.autor}")
print(f"El ISBN del segundo libro es: {libro2.isbn}")
print("\n--- Mostrando información completa ---")
libro1.mostrar_info()
libro2.mostrar_info()
print("Realizado por Flavio Rojas.")
