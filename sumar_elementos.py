def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for elemento_actual in lista_numeros:
        acumulador_suma += elemento_actual
    return acumulador_suma
# Casos de Prueba con assert
print("Probando sumar_elementos...")
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
print("¡Pruebas para sumar_elementos:[1, 2, 3, 4, 5] == 15 pasaron!")
assert sumar_elementos([10, -2, 5]) == 13
print("¡Pruebas para sumar_elementos:[10, -2, 5] == 13 pasaron!")
assert sumar_elementos([]) == 0  # ¡Importante probar con una lista vacía!
print("¡Pruebas para sumar_elementos: [] pasaron!")
assert sumar_elementos([100]) == 100
print("¡Pruebas para sumar_elementos:[100] == 100 pasaron!")
print("¡Pruebas para sumar_elementos pasaron con exito !")
print("prueba realizada por Flavio Rojas")