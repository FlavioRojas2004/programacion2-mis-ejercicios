# 1. Crear la matriz del teclado numérico
teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 2. Imprimir la matriz teclado como una cuadrícula
print("Teclado numérico:")
for fila in teclado:
    for numero in fila:
        print(numero, end="\t")  # Tabulador entre números
    print()  # Nueva línea después de cada fila
# 3. Crear una matriz 5x5 de ceros usando bucles anidados
matriz_5x5_bucles = []
for _ in range(5):
    fila = []
    for _ in range(5):
        fila.append(0)
    matriz_5x5_bucles.append(fila)
# 4. Crear la misma matriz usando comprensión de listas
matriz_5x5_compresion = [[0 for _ in range(5)] for _ in range(5)]
# 5. Imprimir ambas matrices como cuadrícula
print("\nMatriz 5x5 de ceros (usando bucles):")
for fila in matriz_5x5_bucles:
    for numero in fila:
        print(numero, end="\t")
    print()
print("\nMatriz 5x5 de ceros (usando comprensión de listas):")
for fila in matriz_5x5_compresion:
    for numero in fila:
        print(numero, end="\t")
    print()
    # final de la matriz
print("Realizado por Flavio Rojas.")