def contar_apariciones(lista, elemento_buscado):
  contador = 0
  for item in lista:
      if item == elemento_buscado:
          contador += 1
  return contador

def convertir(valor):
  # Intenta convertir a int o float si es posible
  try:
      if "." in valor:
          return float(valor)
      else:
          return int(valor)
  except ValueError:
      return valor.strip()  # Mantener como texto si no es número

# Pruebas con assert
print("\nProbando contar_apariciones...")
assert contar_apariciones([1, 2, 2, 3], 2) == 2
assert contar_apariciones(["1", "2", "2"], "2") == 2
assert contar_apariciones(["a", "b", "a"], "a") == 2
assert contar_apariciones([], "x") == 0
print("¡Pruebas para contar_apariciones pasaron!")

# Entrada del usuario
entrada = input("\nIngresa elementos separados por coma (ej: 1,2,2,3 o rojo,azul): ")
lista_usuario = [convertir(x) for x in entrada.split(",") if x.strip() != ""]

elemento_input = input("¿Qué elemento deseas contar?: ").strip()
elemento_buscado = convertir(elemento_input)

# Contar
cantidad = contar_apariciones(lista_usuario, elemento_buscado)

# Resultado
print(f"El elemento '{elemento_buscado}' aparece {cantidad} veces en la lista.")