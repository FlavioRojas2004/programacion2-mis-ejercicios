def ordenamiento_de_burbuja(lista):
    n = len(lista) # cantidad de elementos en la lista
    for i in range(n - 1): # bucle exterior para las pasadas
        hubo_intercambio = False #marca si hubo intercambio en esta pasada
        for j in range(n - 1 - i): # cada pasada evita revisar los ultimos ya ordenados 
              if lista [j] > lista[j + 1]:
              # intercambio 
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True # se hizo un intercambio    
        if not hubo_intercambio: # si no hubo intercambio, la lista esta ordenada
            break
        return lista # opcional: tambien se pude omitir
# Main 
if __name__ == "__main__":
  numeros = [6, 3, 8, 2, 5,]
  print ("antes:" , numeros)
  ordenamiento_de_burbuja(numeros)
  print ("despues:" , numeros)
print("Realizado por Flavio Rojas.")
