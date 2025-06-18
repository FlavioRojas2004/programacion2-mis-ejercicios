# 1. Crear la matriz 3x3 llamada 'teclado'
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 2. Imprimir la matriz completa
print("Matriz original:")
for fila in teclado:
    print(fila)
# 3. Acceder a elementos específicos
print("\nNúmero en el centro (5):", teclado[1][1])
print("Número en la esquina inferior derecha (9):", teclado[2][2])
# 4. Modificar el número en la esquina superior izquierda (1) por un 0
teclado[0][0] = 0
# 5. Imprimir la matriz de nuevo para ver el cambio
print("\nMatriz modificada:")
for fila in teclado:
    print(fila)
    
print("Realizado por Flavio Rojas.")