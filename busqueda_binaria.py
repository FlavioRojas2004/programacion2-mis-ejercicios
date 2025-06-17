def busqueda_binaria(lista, objetivo):
        # Verifica que la lista esté ordenada
        assert lista == sorted(lista), "La lista debe estar ordenada."
        izquierda = 0
        derecha = len(lista) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = lista[medio]

            if valor_medio == objetivo:
                return medio
            elif valor_medio < objetivo:
                izquierda = medio + 1
            else:
                derecha = medio - 1
        return -1
    # Pruebas automáticas
def pruebas_automaticas():
        print("Probando busqueda_binaria...")
        # Pruebas con números
        numeros = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
        assert busqueda_binaria(numeros, 23) == 5
        assert busqueda_binaria(numeros, 91) == 9
        assert busqueda_binaria(numeros, 2) == 0
        assert busqueda_binaria(numeros, 3) == -1
        assert busqueda_binaria(numeros, 100) == -1
        # Pruebas con letras
        letras = ['ana', 'carlos', 'diana', 'juan', 'maria', 'pedro', 'zulema']
        assert busqueda_binaria(letras, 'juan') == 3
        assert busqueda_binaria(letras, 'ana') == 0
        assert busqueda_binaria(letras, 'zulema') == 6
        assert busqueda_binaria(letras, 'sofia') == -1
        assert busqueda_binaria([], 'luis') == -1
        print("¡Pruebas para busqueda_binaria pasaron!")
    # Entrada del usuario
def main():
        print("=== BÚSQUEDA BINARIA ===")
        entrada = input("Ingresa una lista ordenada de números o palabras separadas por comas: ")
        lista_cruda = [item.strip() for item in entrada.split(',')]
        # Detectar si son números o letras
        es_numerica = all(item.replace('.', '', 1).isdigit() for item in lista_cruda)
        if es_numerica:
            lista_usuario = list(map(float, lista_cruda))  # permite enteros y decimales
            objetivo = float(input("Ingresa el número que deseas buscar: "))
        else:
            lista_usuario = lista_cruda
            objetivo = input("Ingresa la palabra que deseas buscar: ").strip()
        # Verifica si la lista está ordenada
        if lista_usuario != sorted(lista_usuario):
            print(" Error: la lista no está ordenada. La búsqueda binaria solo funciona con listas ordenadas.")
            return
        resultado = busqueda_binaria(lista_usuario, objetivo)
        if resultado != -1:
            print(f" El valor '{objetivo}' se encuentra en el índice {resultado}.")
        else:
            print(f" El valor '{objetivo}' no se encuentra en la lista.")
if __name__ == "__main__":
        pruebas_automaticas()
        main()
print("Realizado por Flavio Rojas.")