# Definimos la función que suma los elementos por cada fila de la matriz
def sumar_por_filas(matriz):
    """
    Esta función recibe una matriz (lista de listas)
    y devuelve una lista con la suma de cada fila,
    usando bucles anidados (sin usar sum()).
    Ejemplo:
    matriz = [[1, 2], [3, 4]] -> [3, 7]
    """
    sumas_filas = []
    for fila in matriz:
        suma_fila_actual = 0
        for elemento in fila:
            suma_fila_actual += elemento
        sumas_filas.append(suma_fila_actual)
    return sumas_filas
# Función de prueba para verificar que sumar_por_filas funciona correctamente
def probar_suma_por_filas():
    print("\nProbando sumar_por_filas...")
    # Caso 1: matriz con 3 filas y 3 columnas
    m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert sumar_por_filas(m1) == [6, 15, 24]  # 1+2+3, 4+5+6, 7+8+9
    # Caso 2: matriz con pares repetidos
    m2 = [[10, 10], [20, 20], [30, 30]]
    assert sumar_por_filas(m2) == [20, 40, 60]
    # Caso borde: matriz vacía
    assert sumar_por_filas([]) == []
    # Caso borde: matriz con filas vacías
    m3 = [[], [], []]
    assert sumar_por_filas(m3) == [0, 0, 0]
    # Caso borde: matriz con una sola fila
    m4 = [[100, 200, 300]]
    assert sumar_por_filas(m4) == [600]

    print("¡Pruebas para sumar_por_filas pasaron!")
# Llamamos a la función para ejecutar las pruebas
probar_suma_por_filas()
print("Realizado por Flavio Rojas.")

