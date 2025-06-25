# Definimos la función que verifica si una matriz es identidad
def es_identidad(matriz):
    """
    Retorna True si la matriz es identidad.
    Una matriz identidad es cuadrada, con 1s en la diagonal y 0s fuera de ella.
    """
    num_filas = len(matriz)
    if num_filas == 0:
        return True  # Una matriz vacía se considera identidad
    # Verificar si la matriz es cuadrada
    for fila in matriz:
        if len(fila) != num_filas:
            return False
    # Verificar los valores de la diagonal y fuera de ella
    for i in range(num_filas):
        for j in range(num_filas):
            if i == j:
                if matriz[i][j] != 1:
                    return False  # La diagonal debe tener 1
            else:
                if matriz[i][j] != 0:
                    return False  # Fuera de la diagonal debe haber 0
    return True
# Función de prueba para verificar que es_identidad funciona correctamente
def probar_es_identidad():
    print("Probando es_identidad...")
    # Caso 1: matriz identidad 3x3
    identidad = [[1, 0, 0],
                 [0, 1, 0],
                 [0, 0, 1]]
    assert es_identidad(identidad) is True
    # Caso 2: matriz con un valor incorrecto en la diagonal
    no_identidad = [[1, 0, 0],
                    [0, 2, 0],
                    [0, 0, 1]]
    assert es_identidad(no_identidad) is False

    # Caso 3: matriz no cuadrada
    no_cuadrada = [[1, 0],
                   [0, 1],
                   [0, 0]]
    assert es_identidad(no_cuadrada) is False
    # Caso 4: matriz vacía
    vacia = []
    assert es_identidad(vacia) is True  # Considerada identidad
    # Caso 5: matriz 1x1 con 1
    una_por_una = [[1]]
    assert es_identidad(una_por_una) is True
    # Caso 6: matriz 1x1 con 0
    una_por_una_invalida = [[0]]
    assert es_identidad(una_por_una_invalida) is False
    print("¡Todas las pruebas de es_identidad pasaron!")
# Ejecutar las pruebas
probar_es_identidad()
print("Realizado por Flavio Rojas.")