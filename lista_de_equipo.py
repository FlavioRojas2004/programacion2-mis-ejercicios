# Ingresar el nombre del grupo
nombre_grupo = "TEAM CHETOS"
# Lista de nombres del equipo
nombres_estudiantes = ["Flavio", "Ana", "Miguel", "Lucía", "Pedro"]
# Lista de nombres de mujeres para identificar el género
nombres_femeninos = ["Ana", "Lucía"]
# Mostrar el nombre del grupo
print(f"Nombre del grupo: {nombre_grupo}")
print("----------------------------------")
# muetsra los nombres de los estudiantes y si son hombres o mujeres
for nombre in nombres_estudiantes:
        if nombre in nombres_femeninos:
            print(f"¡Bienvenida al equipo, {nombre}!")
        else:
            print(f"¡Bienvenido al equipo, {nombre}!")
print("Realizado por Flavio Rojas.")