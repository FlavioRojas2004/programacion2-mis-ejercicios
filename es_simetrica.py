def es_simetrica(matriz):
  """
  Retorna True si la matriz es simétrica, False si no.
  Una matriz simétrica es cuadrada y cumple matriz[i][j] == matriz[j][i].
  """
  num_filas = len(matriz)
  if num_filas == 0:
      return True  # Matriz vacía se considera simétrica
  # Verificar que la matriz sea cuadrada
  for fila in matriz:
      if len(fila) != num_filas:
          return False
  # Comparar elementos para verificar simetría
  for i in range(num_filas):
      for j in range(i + 1, num_filas):  # Solo triangular superior
          if matriz[i][j] != matriz[j][i]:
              return False
  return True
# Función de prueba para verificar que es_simetrica funciona correctamente
def probar_es_simetrica():
  print("Probando es_simetrica...")
  sim = [[1, 7, 3],
         [7, 4, -5],
         [3, -5, 6]]
  no_sim = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
  no_cuadrada = [[1, 2],
                 [3, 4],
                 [5, 6]]
  assert es_simetrica(sim) is True
  assert es_simetrica(no_sim) is False
  assert es_simetrica(no_cuadrada) is False
  # Casos adicionales
  vacia = []
  assert es_simetrica(vacia) is True  # Matriz vacía
  uno_uno = [[1]]
  assert es_simetrica(uno_uno) is True  # Matriz 1x1 es simétrica
  print("¡Pruebas para es_simetrica pasaron!")
# Ejecutar las pruebas
probar_es_simetrica()
print("Realizado por Flavio Rojas.")