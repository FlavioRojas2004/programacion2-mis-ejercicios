def busqueda_lineal(lista, objetivo):
  for indice, valor in enumerate(lista):
      if valor == objetivo:
          return indice
  return -1
def pruebas_automaticas():
  lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
  print("\nProbando busqueda_lineal...")
  assert busqueda_lineal(lista_ordenada, 23) == 5
  assert busqueda_lineal(lista_ordenada, 91) == 9   # Último
  assert busqueda_lineal(lista_ordenada, 2) == 0    # Primero
  assert busqueda_lineal(lista_ordenada, 3) == -1   # No existe
  assert busqueda_lineal(lista_ordenada, 100) == -1 # Fuera de rango (mayor)
  print("¡Pruebas para busqueda_lineal pasaron! ")
def main():
  print("=== BÚSQUEDA LINEAL ===")
  entrada = input("Ingresa una lista de números separados por comas: ")
  lista_usuario = list(map(int, entrada.split(',')))
  objetivo = int(input("Ingresa el número que deseas buscar: "))
  resultado = busqueda_lineal(lista_usuario, objetivo)
  if resultado != -1:
      print(f" El número {objetivo} se encuentra en el índice {resultado}.")
  else:
      print(f" El número {objetivo} no se encuentra en la lista.")
if __name__ == "__main__":
  pruebas_automaticas()
  main() 
print("Realizado por Flavio Rojas.")