edad = int(input("Por favor, ingresa tu edad: "))

def obtener_mensaje_por_edad (edad):
    if edad <=0:
        return "Edad no válida, por favor ingresa un valor positivo."
    elif edad >= 18:
        return "¡Puedes ver películas clasificadas R!"
    elif edad >= 13:
        return "Puedes ver películas clasificadas PG-13."
    else:
        return "Te recomendamos películas clasificadas G o PG."

mensaje_cine = obtener_mensaje_por_edad(edad)
print (mensaje_cine)