def sumar_diagonal_secundaria(matriz):
  """
recibe una matriz cuadrada (misma cantidad de filas y columnas) y retorna la suma de los elementos de la diagonal secundaria. la diagonal secundaria es la que va desde la esquina inferior izquierda hasta la esquina superior derecha.
por ejemplo, en una matriz de 3x3:
[[a, b, c],
 [d, e, f],
 [g, h, i]]
 la diagonal secundaria esta en las pocisiones (2,0), (1,1), (0,2) y la suma seria c + e + g
 """
  n = len(matriz) # numero de filas (y columnas,ya que es una matriz cuadrada)
  suma = 0
  for i in range(n):
    suma += matriz[i][n - 1 - i] #accede al elemento en la posicion 
    (i, n - 1 - i)
  return suma
#funcion de prueba para validar que la suma_diagonal_secundaria funcione correctamente
def probar_sumar_diagonal_secundaria():
  print("\nProbando sumar_diagonal_secundaria...")
  # caso 1 : matriz 3x3 normal
  m1 = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
# diagonal secundaria: 3 + 5 + 7 = 15
  assert sumar_diagonal_secundaria(m1) == 15
  # caso 2: matriz 2x2
m2 = [[10, 1],
      [2, 20]]
# diagonal secundaria: 1 + 2 = 3
assert sumar_diagonal_secundaria(m2) == 3
# caso 3: matriz 1x1
m3 = [[42]]
# solo hay un elemento: 42
assert sumar_diagonal_secundaria(m3) == 42
print("¡Todos los casos de prueba pasados!")
#llamar a la funcion de prueba
print("Realizado por Flavio Rojas.")

  