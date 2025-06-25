# Definimos la función que transpone una matriz
def transponer_matriz(matriz):
    """
    Esta función recibe una matriz (lista de listas) y
    devuelve una nueva matriz que es la transpuesta de la original.
    No modifica la matriz original.
    """
    if not matriz or not matriz[0]:  # Matriz vacía o filas vacías
        return []
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    matriz_transpuesta = []
    for j in range(num_columnas):  # Itera sobre las columnas originales
        nueva_fila = []
        for i in range(num_filas):  # Itera sobre las filas originales
            nueva_fila.append(matriz[i][j])
        matriz_transpuesta.append(nueva_fila)
    return matriz_transpuesta
# Función de prueba para verificar que transponer_matriz funciona correctamente
def probar_transponer_matriz():
    print("Probando transponer_matriz...")
    # Caso 1: matriz 2x3
    m1 = [[1, 2, 3], [4, 5, 6]]
    t1 = transponer_matriz(m1)
    assert t1 == [[1, 4], [2, 5], [3, 6]]
    print("Prueba 1 (2x3) pasada!")
    # Caso 2: matriz 3x2
    m2 = [[7, 8], [9, 10], [11, 12]]
    t2 = transponer_matriz(m2)
    assert t2 == [[7, 9, 11], [8, 10, 12]]
    print("Prueba 2 (3x2) pasada!")
    # Caso 3: matriz cuadrada 2x2
    m3 = [[1, 2], [3, 4]]
    t3 = transponer_matriz(m3)
    assert t3 == [[1, 3], [2, 4]]
    print("Prueba 3 (2x2) pasada!")
    # Caso 4: matriz de 1x4
    m4 = [[10, 20, 30, 40]]
    t4 = transponer_matriz(m4)
    assert t4 == [[10], [20], [30], [40]]
    print("Prueba 4 (1x4) pasada!")
    # Caso 5: matriz de 4x1
    m5 = [[5], [6], [7], [8]]
    t5 = transponer_matriz(m5)
    assert t5 == [[5, 6, 7, 8]]
    print("Prueba 5 (4x1) pasada!")
    # Caso 6: matriz vacía
    m6 = []
    t6 = transponer_matriz(m6)
    assert t6 == []
    print("Prueba 6 (vacía) pasada!")
    # Caso 7: matriz con filas vacías
    m7 = [[], [], []]
    t7 = transponer_matriz(m7)
    assert t7 == []
    print("Prueba 7 (filas vacías) pasada!")
    print("¡Todas las pruebas de transponer_matriz pasaron!")
# Ejecutar las pruebas
probar_transponer_matriz()
print("Realizado por Flavio Rojas.")
