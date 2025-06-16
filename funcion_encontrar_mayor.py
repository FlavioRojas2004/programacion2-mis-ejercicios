def encontrar_mayor(lista_numeros):
    # Caso especial: lista vacía
    if not lista_numeros:
        return None
    # Asignamos el primer elemento como mayor temporal
    mayor_temporal = lista_numeros[0]
    # Recorremos la lista desde el segundo elemento
    for elemento_actual in lista_numeros[1:]:
        if elemento_actual > mayor_temporal:
            mayor_temporal = elemento_actual
    # Retornamos el mayor encontrado
    return mayor_temporal
# Pruebas
print("\nProbando encontrar_mayor...")
assert encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9
print("Prueba 1 pasada: encontrar_mayor([1, 9, 2, 8, 3, 7]) == 9")
assert encontrar_mayor([-1, -9, -2, -8]) == -1
print("Prueba 2 pasada: encontrar_mayor([-1, -9, -2, -8]) == -1")
assert encontrar_mayor([42, 42, 42]) == 42
print("Prueba 3 pasada: encontrar_mayor([42, 42, 42]) == 42")
assert encontrar_mayor([]) == None  # Prueba del caso especial
print("Prueba 4 pasada: encontrar_mayor([]) == None")
assert encontrar_mayor([5]) == 5
print("Prueba 5 pasada: encontrar_mayor([5]) == 5")
print("¡Pruebas para encontrar_mayor pasaron!")
print("Realizado por: Flavio Rojas")