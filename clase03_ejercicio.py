# Solicitar la edad al
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar la edad y mostrar el mensaje correspondiente
if edad < 0:
    print("Edad no válida, por favor ingresa un valor positivo.")
elif edad >= 18:
    print("¡Puedes ver películas clasificadas R!")
elif edad >= 13:
    print("Puedes ver películas clasificadas PG-13.")
else:
    print("Te recomendamos películas clasificadas G o PG.")
