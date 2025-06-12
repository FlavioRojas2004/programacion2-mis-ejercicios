def invertir_lista(lista_original):
    lista_invertida = []
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])
    return lista_invertida
# Pruebas con assert
print("\nProbando invertir_lista con assert...")
assert invertir_lista([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []
assert invertir_lista([42]) == [42]
print("¡Todas las pruebas pasaron!")
# Entrada del usuario
entrada = input("\nIngresa elementos separados por coma (ejemplo: 1,2,3,4): ")
lista_usuario = [x.strip() for x in entrada.split(",") if x.strip() != ""]
# Invertir la lista
resultado = invertir_lista(lista_usuario)
# Mostrar resultados
print("Lista original:", lista_usuario)
print("Lista invertida:", resultado)