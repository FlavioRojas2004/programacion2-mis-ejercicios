numero_tabla = int(input("Ingresa un número para ver su tabla de multiplicar que desea realizar: ")) #Pide la insercion de los datos a realizar 
print(f"--- Tabla del numero {numero_tabla} ---") #
for i in range(1, 11): # i tomará valores de 1 a 10
 resultado = numero_tabla * i
 print(f"{numero_tabla} x {i} = {resultado}") #Muestra el resultado en consola 
print("Realizado po Flavio Rojas.")      