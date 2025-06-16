# Lista con tus notas
notas = [85, 90, 78, 92, 88]
# Mostrar todas las notas
print("Tus notas son:")
for i in range(len(notas)):
    print(f"Nota {i + 1}: {notas[i]}")
# Calcular el promedio
promedio = sum(notas) / len(notas)
print(f"\nPromedio final: {promedio}")
print("-------------------------------------")

# Lista de hobbies 
hobbies = ["Leer libros", "Jugar fútbol", "Escuchar música"]
# Mostrar los hobbies
print("Estos son mis 3 hobbies favoritos:")
print("-----------------------------------")
for i, hobby in enumerate(hobbies, start=1):
    print(f"Hobby {i}: {hobby}")
print("-----------------------------------")
print("Flavio Rojas.")

