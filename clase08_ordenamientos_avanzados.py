# clase08_ordenamientos_avanzados.py

def merge_sort(lista):
    # Paso VENCER (Condición base de la recursión)
    if len(lista) <= 1:
        return lista

    # Paso 1: DIVIDIR
    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]
    mitad_derecha = lista[medio:]

    # Paso 2: VENCER (Llamadas recursivas)
    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    # Paso 3: COMBINAR
    print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")

    # Por ahora devolvemos la lista original sin mezclar
    return lista  # ⚠️ Esto no está ordenado aún


# --- Función de Mezcla (placeholder) ---
def merge(izquierda, derecha):
    # Aquí iría la lógica para mezclar dos listas ordenadas
    pass  # No implementado todavía


# MAIN: Para probar el esqueleto de MergeSort
if __name__ == "__main__":
    lista_prueba = [38, 27, 43, 3, 9, 82, 10]
    print("Lista original:", lista_prueba)
    resultado = merge_sort(lista_prueba)
    print("Resultado (no ordenado aún):", resultado)
print("Realizado por Flavio Rojas.")